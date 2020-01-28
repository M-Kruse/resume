from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from django.http import JsonResponse
from django.views.generic import TemplateView

from .models import Employment, Applicant, Experience, Education, Resume

class IndexView(generic.ListView):
    template_name = 'viewer/index.html'

    def get_queryset(self):
        """Return the Employment objects questions."""
        return Employment.objects.all()

    
class HTMLView(generic.ListView):
    model = Employment
    template_name = 'viewer/resume.html'
    #context_object_name = 'employment_list'
    
    def get_queryset(self):
        """Return the Employment objects questions."""
        return Employment.objects.all()

    def get_context_data(self, **kwargs):
        """Call the base implementation first to get a context """
        context = super(HTMLView, self).get_context_data(**kwargs)
        """ Add extra context from another model """
        context['applicant'] = Applicant.objects.get()
        return context

class JSONResponseMixin:

    def render_to_json_response(self, context, **response_kwargs):

        return JsonResponse(
            self.get_data(context),
            **response_kwargs
        )

    def get_data(self, context):
        return context

class JSONView(JSONResponseMixin, TemplateView):

    def create_resume_json(self):
        applicant = Applicant.objects.get()
        resume_json = {
            "contact_info": {
                "name": applicant.name,
                "email": applicant.email,
                "phone": applicant.phone,
                },
            "employments":[],
            "experiences":[],
            "education":[],
            "references":[]
            }
        employments = Employment.objects.all()
        for e in employments:
            employment_json = {
                    "company_name": e.company_name,
                    "job_title": e.job_title,
                    "start_date": e.start_date,
                    "start_date": e.end_date,
                    "duties": [],
                    "projects": [],
                }
            for d in e.duties.all():
                employment_json['duties'].append(d.description)

            for p in e.projects.all():
                employment_json['projects'].append(p.description)
            resume_json['employments'].append(employment_json)
        experiences = applicant.experiences.all()
        d_list = []
        for x in experiences:
            d_list.append(x.domain.name)
        d_list = set(d_list)
        for domain in d_list:
            x_list = []
            for x in experiences:
                if x.domain.name == domain:
                    x_list.append(x.name)
            domains_json = {
                domain: x_list
                }
            resume_json['experiences'].append(domains_json)
        education = Education.objects.all()
        for e in education:
            education_json = {
                "school": e.name,
                "level": e.level,
                "year": e.year
                }
            resume_json['education'].append(education_json)
        refs = applicant.reference.all()
        for r in refs:
            reference_json = {
                "name": r.name,
                "employment": r.employment.company_name,
                "contact": r.contact,
            }
            print(reference_json)
            resume_json['references'].append(reference_json)
        return resume_json

    def render_to_response(self, context, **response_kwargs):
        return self.render_to_json_response(self.create_resume_json(), **response_kwargs)

class ResumeListView(generic.ListView):
    model = Resume
    template_name = 'viewer/resume_list.html'
    context_object_name = 'resume_list'
    
    def get_queryset(self):
        """Return the Employment objects questions."""
        return Resume.objects.all()

    # def get_context_data(self, **kwargs):
    #     """Call the base implementation first to get a context """
    #     context = super(HTMLView, self).get_context_data(**kwargs)
    #     """ Add extra context from another model """
    #     context['applicant'] = Applicant.objects.get()
    #     return context


from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import ResumeForm

def new_resume(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ResumeForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
                name = form.cleaned_data['name']
                applicant = form.cleaned_data['applicant']
                output_format = form.cleaned_data['output_format']
                style = form.cleaned_data['style']
                r = Resume(name=name, applicant=applicant, output_format=output_format, style=style)
                r.save()
                return HttpResponseRedirect('/nextform/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ResumeForm()

    return render(request, 'viewer/resume_form.html', {'form': form})

# class NewResumeView(generic.ListView):
#     model = Resume
#     template_name = 'viewer/new_resume.html'
    
#     def get_queryset(self):
#         """Return the Resume objects."""
#         return Resume.objects.all()
