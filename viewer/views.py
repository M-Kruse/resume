from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from django.views.generic import TemplateView

from .models import Employment, Employee, Experience

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

