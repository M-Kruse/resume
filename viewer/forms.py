from django.forms import ModelForm
from viewer.models import Employment, Applicant, Experience, Education, Resume, Domain, Reference, Project, Duty, Template
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class ResumeForm(ModelForm):
	class Meta:
		model = Resume
		fields = ['name', 'applicant', 'output_format', 'template' ]

class ApplicantForm(ModelForm):
	class Meta:
		model = Applicant
		fields = ['name', 'email', 'phone', 'employment', 'experiences', 'education', 'reference']

class DomainForm(ModelForm):
	class Meta:
		model = Domain
		fields = ['name']

class ExperienceForm(ModelForm):
	class Meta:
		model = Experience
		fields = ['name', 'domain']

class EducationForm(ModelForm):
	class Meta:
		model = Education
		fields = ['name', 'level', 'year']

class ReferenceForm(ModelForm):
	class Meta:
		model = Reference
		fields = ['name', 'employment', 'contact']

class EmploymentForm(ModelForm):
	class Meta:
		model = Employment
		fields = ['company_name', 'job_title', 'start_date', 'end_date', 'leave_reason', 'duties', 'projects']

class ProjectForm(ModelForm):
	class Meta:
		model = Project
		fields = ['description']

class DutyForm(ModelForm):
	class Meta:
		model = Duty
		fields = ['description']

class TemplateForm(ModelForm):
	class Meta:
		model = Template
		fields = ['name', 'file']

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')