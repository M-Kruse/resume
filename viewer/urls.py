from django.urls import path
from django.conf.urls import url
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from . import views

app_name = 'resume'
urlpatterns = [
	path('', login_required(views.IndexView.as_view()), name="index"),
    path('html/<int:pk>', views.HTMLView.as_view(), name="html"),
    path('json/<int:pk>', views.JSONView.as_view(), name="json"),
    path('docx/<int:pk>', views.build_resume_from_docx_template, name="docx"),
    path('resume/', login_required(views.ResumeListView.as_view()), name="resumes"),
    path('resume/new/', login_required(views.new_resume), name="newResume"),
    path('resume/wizard', login_required(views.ResumeWizardView.as_view()), name="resumeWizard"),
    path('resume/edit/<int:pk>', login_required(views.ResumeUpdateView.as_view()), name='updateResume'),
    path('resume/delete/<int:pk>', login_required(views.ResumeDeleteView.as_view()), name='deleteResume'),
    path('applicant/', login_required(views.ApplicantListView.as_view()), name="applicants"),
    path('applicant/new', login_required(views.new_applicant), name="newApplicant"),
    path('applicant/edit/<int:pk>', login_required(views.ApplicantUpdateView.as_view()), name='updateApplicant'),
    path('applicant/delete/<int:pk>', login_required(views.ApplicantDeleteView.as_view()), name='deleteApplicant'),
    path('domain/', login_required(views.DomainListView.as_view()), name="domain"),
    path('domain/new', login_required(views.new_domain), name="newDomain"),
    path('domain/edit/<int:pk>', login_required(views.DomainUpdateView.as_view()), name='updateDomain'),
    path('domain/delete/<int:pk>', login_required(views.DomainDeleteView.as_view()), name='deleteDomain'),
    path('experience/', login_required(views.ExperienceListView.as_view()), name='xp'),
    path('experience/new', login_required(views.new_experience), name='newXP'),
    path('experience/edit/<int:pk>', login_required(views.ExperienceUpdateView.as_view()), name='updateXP'),
    path('experience/delete/<int:pk>', login_required(views.ExperienceDeleteView.as_view()), name='deleteXP'),
    path('education/', login_required(views.EducationListView.as_view()), name='edus'),
    path('education/new', login_required(views.new_education), name='newEDU'),
    path('education/edit/<int:pk>', login_required(views.EducationUpdateView.as_view()), name='updateEDU'),
    path('education/delete/<int:pk>', login_required(views.EducationDeleteView.as_view()), name='deleteEDU'),
    path('reference/', login_required(views.ReferenceListView.as_view()), name='refs'),
    path('reference/new', login_required(views.new_reference), name='newRef'),
    path('reference/edit/<int:pk>', login_required(views.ReferenceUpdateView.as_view()), name='updateRef'),
    path('reference/delete/<int:pk>', login_required(views.ReferenceDeleteView.as_view()), name='deleteRef'),
    path('employment/', login_required(views.EmploymentListView.as_view()), name='employments'),
    path('employment/new', login_required(views.new_employment), name='newEmploy'),
    path('employment/edit/<int:pk>', login_required(views.EmploymentUpdateView.as_view()), name='updateEmploy'),
    path('employment/delete/<int:pk>', login_required(views.EmploymentDeleteView.as_view()), name='deleteEmploy'),
    path('duty/', login_required(views.DutyListView.as_view()), name='duties'),
    path('duty/new', login_required(views.new_duty), name='newDuty'),
    path('duty/edit/<int:pk>', login_required(views.DutyUpdateView.as_view()), name='updateDuty'),
    path('duty/delete/<int:pk>', login_required(views.DutyDeleteView.as_view()), name='deleteDuty'),
    path('project/', login_required(views.ProjectListView.as_view()), name='projects'),
    path('project/new', login_required(views.new_project), name='newProject'),
    path('project/edit/<int:pk>', login_required(views.ProjectUpdateView.as_view()), name='updateProject'),
    path('project/delete/<int:pk>', login_required(views.ProjectDeleteView.as_view()), name='deleteProject'),
    path('template/', login_required(views.TemplateListView.as_view()), name='templates'),
    path('template/new', login_required(views.new_template), name='newTemplate'),
    path('template/edit/<int:pk>', login_required(views.TemplateUpdateView.as_view()), name='updateTemplate'),
    path('template/delete/<int:pk>', login_required(views.TemplateDeleteView.as_view()), name='deleteTemplate'),
    path('template/view/<int:pk>', login_required(views.view_template), name='previewTemplate'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    #This seems to be the latest convention for urls (vs using path() )
    url(r'^signup/$', views.signup, name='signup'),

]