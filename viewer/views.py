from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from django.http import JsonResponse
from django.views.generic import TemplateView, UpdateView, DeleteView

from .models import Employment, Applicant, Experience, Education, Resume, Domain, Experience, Reference, Project, Duty

from .forms import ResumeForm, ApplicantForm, DomainForm, ExperienceForm, EducationForm, ReferenceForm, EmploymentForm, ProjectForm, DutyForm

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
        resume = Resume.objects.get(pk=self.kwargs.get('pk'))
        return resume.applicant.employment.all

    def get_context_data(self, **kwargs):
        resume = Resume.objects.get(pk=self.kwargs.get('pk'))
        """Call the base implementation first to get a context """
        context = super(HTMLView, self).get_context_data(**kwargs)
        """ Add extra context from another model """
        context['applicant'] = Applicant.objects.get(pk=resume.applicant.id)
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
        resume = Resume.objects.get(pk=self.kwargs.get('pk'))
        applicant = Applicant.objects.get(pk=resume.applicant.id)
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
        return Resume.objects.all()

def new_resume(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
                name = form.cleaned_data['name']
                applicant = form.cleaned_data['applicant']
                output_format = form.cleaned_data['output_format']
                style = form.cleaned_data['style']
                r = Resume(name=name, applicant=applicant, output_format=output_format, style=style)
                r.save()
                return HttpResponseRedirect('/resume/')
    else:
        form = ResumeForm()
    return render(request, 'viewer/resume_form.html', {'form': form})

class ApplicantListView(generic.ListView):
    model = Applicant
    template_name = 'viewer/applicant_list.html'
    context_object_name = 'app_list'
    
    def get_queryset(self):
        return Applicant.objects.all()

def new_applicant(request):
    if request.method == 'POST':
        form = ApplicantForm(request.POST)
        if form.is_valid():
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
                phone = form.cleaned_data['phone']                
                a = Applicant(name=name, email=email, phone=phone, owner=request.user)
                a.save()
                return HttpResponseRedirect('/applicant/')
    else:
        form = ApplicantForm()

    return render(request, 'viewer/applicant_form.html', {'form': form})

class DomainListView(generic.ListView):
    model = Domain
    template_name = 'viewer/domain_list.html'
    context_object_name = 'domain_list'
    
    def get_queryset(self):
        return Domain.objects.all()

def new_domain(request):
    if request.method == 'POST':
        form = DomainForm(request.POST)
        if form.is_valid():
                name = form.cleaned_data['name']
                d = Domain(name=name)
                d.save()
                return HttpResponseRedirect('/experience/')
    else:
        form = DomainForm()
    return render(request, 'viewer/xp_domain_form.html', {'form': form})

class ExperienceListView(generic.ListView):
    model = Experience
    template_name = 'viewer/xp_list.html'
    context_object_name = 'xp_list'
    
    def get_queryset(self):
        return Experience.objects.all()

def new_experience(request):
    if request.method == 'POST':
        form = ExperienceForm(request.POST)
        if form.is_valid():
                name = form.cleaned_data['name']
                domain = form.cleaned_data['domain']
                e = Experience(name=name, domain=domain)
                e.save()
                return HttpResponseRedirect('/experience/')
    else:
        form = ExperienceForm()
    return render(request, 'viewer/xp_form.html', {'form': form})

class EducationListView(generic.ListView):
    model = Education
    template_name = 'viewer/edu_list.html'
    context_object_name = 'edu_list'
    
    def get_queryset(self):
        return Education.objects.all()

def new_education(request):
    if request.method == 'POST':
        form = EducationForm(request.POST)
        if form.is_valid():
                name = form.cleaned_data['name']
                level = form.cleaned_data['level']
                year = form.cleaned_data['year']
                e = Education(name=name, level=level, year=year)
                e.save()
                return HttpResponseRedirect('/education/')
    else:
        form = EducationForm()
    return render(request, 'viewer/edu_form.html', {'form': form})

class ReferenceListView(generic.ListView):
    model = Reference
    template_name = 'viewer/ref_list.html'
    context_object_name = 'ref_list'
    
    def get_queryset(self):
        return Reference.objects.all()

def new_reference(request):
    if request.method == 'POST':
        form = ReferenceForm(request.POST)
        if form.is_valid():
                name = form.cleaned_data['name']
                employment = form.cleaned_data['employment']
                contact = form.cleaned_data['contact']
                r = Reference(name=name, employment=employment, contact=contact)
                r.save()
                return HttpResponseRedirect('/reference/')
    else:
        form = ReferenceForm()

    return render(request, 'viewer/ref_form.html', {'form': form})

class EmploymentListView(generic.ListView):
    model = Employment
    template_name = 'viewer/employment_list.html'
    context_object_name = 'employment_list'
    
    def get_queryset(self):
        return Employment.objects.all()

def new_employment(request):
    if request.method == 'POST':
        form = EmploymentForm(request.POST)
        if form.is_valid():
                company_name = form.cleaned_data['company_name']
                job_title = form.cleaned_data['job_title']
                start_date = form.cleaned_data['start_date']
                end_date = form.cleaned_data['end_date']
                leave_reason = form.cleaned_data['leave_reason']
                duties = form.cleaned_data['duties']
                projects = form.cleaned_data['projects']
                e = Employment(
                            company_name=company_name, 
                            job_title=job_title,
                            start_date=start_date,
                            end_date=end_date,
                            leave_reason=leave_reason,
                    )
                e.save()
                e.duties.set(duties)
                e.projects.set(projects)
                return HttpResponseRedirect('/employment/')
    else:
        form = EmploymentForm()

    return render(request, 'viewer/employment_form.html', {'form': form})

class ProjectListView(generic.ListView):
    model = Project
    template_name = 'viewer/project_list.html'
    context_object_name = 'project_list'
    
    def get_queryset(self):
        return Project.objects.all()

def new_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            desc = form.cleaned_data['description']
            p = Project(description=desc)
            p.save()
            return HttpResponseRedirect('/project/')
    else:
        form = ProjectForm()
    return render(request, 'viewer/project_form.html', {'form': form})

class DutyListView(generic.ListView):
    model = Duty
    template_name = 'viewer/duty_list.html'
    context_object_name = 'duty_list'
    
    def get_queryset(self):
        return Duty.objects.all()

def new_duty(request):
    if request.method == 'POST':
        form = DutyForm(request.POST)
        if form.is_valid():
            desc = form.cleaned_data['description']
            d = Duty(description=desc)
            d.save()
            return HttpResponseRedirect('/duty/')
    else:
        form = DutyForm()
    return render(request, 'viewer/duty_form.html', {'form': form})

class DomainUpdateView(UpdateView):
   model = Domain
   form_class = DomainForm
   template_name = 'viewer/domain_update_form.html'

   def form_valid(self, form):
      self.object = form.save(commit=False)
      # Any manual settings go here
      self.object.save()
      return HttpResponseRedirect('/experience/')
      #return HttpResponseRedirect(self.object.get_absolute_url())
   
   def dispatch(self, request, *args, **kwargs):
     return super(DomainUpdateView, self).dispatch(request, *args, **kwargs)

class ExperienceUpdateView(UpdateView):
   model = Experience
   form_class = ExperienceForm
   template_name = 'viewer/xp_update_form.html'

   def form_valid(self, form):
      self.object = form.save(commit=False)
      # Any manual settings go here
      self.object.save()
      return HttpResponseRedirect('/experience/')
      #return HttpResponseRedirect(self.object.get_absolute_url())
   
   def dispatch(self, request, *args, **kwargs):
     return super(ExperienceUpdateView, self).dispatch(request, *args, **kwargs)

class EducationUpdateView(UpdateView):
   model = Education
   form_class = EducationForm
   template_name = 'viewer/edu_update_form.html'

   def form_valid(self, form):
      self.object = form.save(commit=False)
      # Any manual settings go here
      self.object.save()
      return HttpResponseRedirect('/education/')
      #return HttpResponseRedirect(self.object.get_absolute_url())
   
   def dispatch(self, request, *args, **kwargs):
     return super(EducationUpdateView, self).dispatch(request, *args, **kwargs)

class ReferenceUpdateView(UpdateView):
   model = Reference
   form_class = ReferenceForm
   template_name = 'viewer/ref_update_form.html'

   def form_valid(self, form):
      self.object = form.save(commit=False)
      # Any manual settings go here
      self.object.save()
      return HttpResponseRedirect('/reference/')
      #return HttpResponseRedirect(self.object.get_absolute_url())
   
   def dispatch(self, request, *args, **kwargs):
     return super(ReferenceUpdateView, self).dispatch(request, *args, **kwargs)

class EmploymentUpdateView(UpdateView):
   model = Employment
   form_class = EmploymentForm
   template_name = 'viewer/employment_update_form.html'

   def form_valid(self, form):
      self.object = form.save(commit=False)
      # Any manual settings go here
      self.object.save()
      return HttpResponseRedirect('/employment/')
      #return HttpResponseRedirect(self.object.get_absolute_url())
   
   def dispatch(self, request, *args, **kwargs):
     return super(EmploymentUpdateView, self).dispatch(request, *args, **kwargs)

class ProjectUpdateView(UpdateView):
   model = Project
   form_class = ProjectForm
   template_name = 'viewer/project_update_form.html'

   def form_valid(self, form):
      self.object = form.save(commit=False)
      # Any manual settings go here
      self.object.save()
      return HttpResponseRedirect('/project/')
      #return HttpResponseRedirect(self.object.get_absolute_url())
   
   def dispatch(self, request, *args, **kwargs):
     return super(ProjectUpdateView, self).dispatch(request, *args, **kwargs)

class DutyUpdateView(UpdateView):
   model = Duty
   form_class = DutyForm
   template_name = 'viewer/duty_update_form.html'

   def form_valid(self, form):
      self.object = form.save(commit=False)
      # Any manual settings go here
      self.object.save()
      return HttpResponseRedirect('/duty/')
      #return HttpResponseRedirect(self.object.get_absolute_url())
   
   def dispatch(self, request, *args, **kwargs):
     return super(DutyUpdateView, self).dispatch(request, *args, **kwargs)

class ApplicantUpdateView(UpdateView):
   model = Applicant
   form_class = ApplicantForm
   template_name = 'viewer/app_update_form.html'

   def form_valid(self, form):
      self.object = form.save(commit=False)
      # Any manual settings go here
      self.object.save()
      return HttpResponseRedirect('/applicant/')
      #return HttpResponseRedirect(self.object.get_absolute_url())
   
   def dispatch(self, request, *args, **kwargs):
     return super(ApplicantUpdateView, self).dispatch(request, *args, **kwargs)

class ResumeUpdateView(UpdateView):
   model = Resume
   form_class = ResumeForm
   template_name = 'viewer/resume_update_form.html'

   def form_valid(self, form):
      self.object = form.save(commit=False)
      # Any manual settings go here
      self.object.save()
      return HttpResponseRedirect('/resume/')
      #return HttpResponseRedirect(self.object.get_absolute_url())
   
   def dispatch(self, request, *args, **kwargs):
     return super(ResumeUpdateView, self).dispatch(request, *args, **kwargs)

class DomainDeleteView(DeleteView):
   model = Domain

   def get_success_url(self):
      return reverse('resume:xp')  

   def dispatch(self, request, *args, **kwargs):
      return super(DomainDeleteView, self).dispatch(request, *args, **kwargs)

class ExperienceDeleteView(DeleteView):
   model = Experience

   def get_success_url(self):
      return reverse('resume:xp')  

   def dispatch(self, request, *args, **kwargs):
      return super(ExperienceDeleteView, self).dispatch(request, *args, **kwargs)

class ResumeDeleteView(DeleteView):
   model = Resume

   def get_success_url(self):
      return reverse('resume:resumes')  

   def dispatch(self, request, *args, **kwargs):
      return super(ResumeDeleteView, self).dispatch(request, *args, **kwargs)

class ApplicantDeleteView(DeleteView):
   model = Applicant

   def get_success_url(self):
      return reverse('resume:applicants')  

   def dispatch(self, request, *args, **kwargs):
      return super(ApplicantDeleteView, self).dispatch(request, *args, **kwargs)

class EmploymentDeleteView(DeleteView):
   model = Employment

   def get_success_url(self):
      return reverse('resume:employments')  

   def dispatch(self, request, *args, **kwargs):
      return super(EmploymentDeleteView, self).dispatch(request, *args, **kwargs)

class ReferenceDeleteView(DeleteView):
   model = Reference

   def get_success_url(self):
      return reverse('resume:refs')  

   def dispatch(self, request, *args, **kwargs):
      return super(ReferenceDeleteView, self).dispatch(request, *args, **kwargs)

class EducationDeleteView(DeleteView):
   model = Education

   def get_success_url(self):
      return reverse('resume:edus')  

   def dispatch(self, request, *args, **kwargs):
      return super(EducationDeleteView, self).dispatch(request, *args, **kwargs)

class ProjectDeleteView(DeleteView):
   model = Project

   def get_success_url(self):
      return reverse('resume:projects')  

   def dispatch(self, request, *args, **kwargs):
      return super(ProjectsDeleteView, self).dispatch(request, *args, **kwargs)      

class DutyDeleteView(DeleteView):
   model = Duty

   def get_success_url(self):
      return reverse('resume:duties')  

   def dispatch(self, request, *args, **kwargs):
      return super(DutyDeleteView, self).dispatch(request, *args, **kwargs)