from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Employment

class IndexView(generic.ListView):
    template_name = 'viewer/index.html'
    context_object_name = 'employment_list'
    def get_queryset(self):
        """Return the Employment objects questions."""
        return Employment.objects.all()