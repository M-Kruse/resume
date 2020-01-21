from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Employment, Employee

class IndexView(generic.ListView):
    model = Employment
    template_name = 'viewer/index.html'
    context_object_name = 'employment_list'
    def get_queryset(self):
        """Return the Employment objects questions."""
        return Employment.objects.all()
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(IndexView, self).get_context_data(**kwargs)
        # Add extra context from another model
        context['employee'] = Employee.objects.get()
        return context