from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from django.http import JsonResponse
from django.views.generic import TemplateView

from .models import Employment, Employee, Experience, Education

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
        context['employee'] = Employee.objects.get()
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
        employee = Employee.objects.get()
        resume_json = {
            "contact_info": {
                "name": employee.name,
                "email": employee.email,
                "phone": employee.phone,
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
        domains = employee.domains.all()
        for d in domains:
            experiences = []
            for e in d.experiences.all():
                experiences.append(e.name)
            domains_json = {
                d.name: experiences
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
        refs = employee.reference.all()
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
                