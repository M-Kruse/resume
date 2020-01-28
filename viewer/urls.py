from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'resume'
urlpatterns = [
	path('', views.IndexView.as_view(), name="index"),
    path('html/', views.HTMLView.as_view(), name="html"),
    path('json/', views.JSONView.as_view(), name="json"),
    path('resume/', views.ResumeListView.as_view(), name="resumes"),
    path('resume/new/', views.new_resume, name="new"),
]