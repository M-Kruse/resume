from django.forms import ModelForm
from viewer.models import Employment, Applicant, Experience, Education, Resume


class ResumeForm(ModelForm):
	class Meta:
		model = Resume
		fields = ['name', 'applicant', 'output_format', 'style' ]

class ApplicantForm(ModelForm):
	class Meta:
		model = Applicant
		fields = ['name', 'email', 'phone', 'employment', 'experiences', 'education', 'reference']



