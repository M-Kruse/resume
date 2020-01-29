from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'resume'
urlpatterns = [
	path('', views.IndexView.as_view(), name="index"),
    path('html/', views.HTMLView.as_view(), name="html"),
    path('json/', views.JSONView.as_view(), name="json"),
    path('resume/', views.ResumeListView.as_view(), name="resumes"),
    path('resume/new/', views.new_resume, name="newResume"),
    path('applicant/', views.ApplicantListView.as_view(), name="applicant"),
    path('applicant/new', views.new_applicant, name="newApplicant"),
    path('domain/', views.DomainListView.as_view(), name="domain"),
    path('domain/new', views.new_domain, name="newDomain"),
    path('experience/', views.ExperienceListView.as_view(), name='xp'),
    path('experience/new', views.new_experience, name='newXP'),
    path('education/', views.EducationListView.as_view(), name='edu'),
    path('education/new', views.new_education, name='newEDU'),
    path('reference/', views.ReferenceListView.as_view(), name='ref'),
    path('reference/new', views.new_reference, name='newRef'),
    path('employment/', views.EmploymentListView.as_view(), name='employ'),
    path('employment/new', views.new_employment, name='newEmploy'),
]