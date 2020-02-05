import datetime

from django.db import models

from django.contrib.auth.models import User
from django.views.generic.edit import UpdateView


class Employment(models.Model):
    company_name = models.CharField(max_length=128, default=None)
    job_title = models.CharField(max_length=64, default=None)
    start_date = models.DateField('Employment Start Date', default=None)
    end_date = models.DateField('Employment End Date', default=None)
    leave_reason = models.CharField(max_length=512, default=None)
    duties = models.ManyToManyField('Duty', related_name='duties')
    projects = models.ManyToManyField('Project', related_name='projects')

    def __str__(self):
        return self.company_name

class Duty(models.Model):
    description = models.CharField(max_length=256, default=None, blank=True)
   
    def __str__(self):
        return self.description

class Project(models.Model):
    description = models.CharField(max_length=256, default=None, blank=True)

    def __str__(self):
        return self.description

class Applicant(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=128)
    phone = models.CharField(max_length=16)
    experiences = models.ManyToManyField('Experience', related_name='domains', blank=True)
    education = models.ManyToManyField('Education', related_name='education', blank=True)
    reference = models.ManyToManyField('Reference', related_name='references', blank=True)
    employment = models.ManyToManyField('Employment', related_name='employments', blank=True)

    def __str__(self):
        return self.name

class Domain(models.Model):
    name = models.CharField(max_length=64, blank=False)

    def __str__(self):
        return self.name

class Experience(models.Model):
    name = models.CharField(max_length=64, default=None, blank=False)
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Education(models.Model):
    name = models.CharField(max_length=64, default="N/A", blank=False)
    level = models.CharField(max_length=64, default="N/A", blank=True)
    year = models.DateField('Graduation Year', default=None, blank=False)

    def __str__(self):
        return self.name

class Reference(models.Model):
    name = models.CharField(max_length=64, blank=False)
    contact = models.CharField(max_length=64, default="Availabe On Request", blank=True)
    employment = models.ForeignKey(Employment, on_delete=models.CASCADE)
    #employment = models.ManyToManyField('Employment', related_name='employments', blank=True)
    
    def __str__(self):
        return self.name

class Style(models.Model):
    name = models.CharField(max_length=64, blank=False, default="Default")

    def __str__(self):
        return self.name

class Resume(models.Model):
    name = models.CharField(max_length=64, blank=False)
    HTML = 'HTML'
    JSON = 'JSON'
    DOCX = 'DOCX'
    PDF = 'PDF'
    FORMATS = [(HTML, HTML), (JSON, JSON), (DOCX, DOCX), (PDF, PDF)]
    output_format = models.CharField(max_length=64,
                            blank=False,
                            choices=FORMATS,
                            default=JSON)
    applicant = models.ForeignKey('Applicant', on_delete=models.CASCADE)
    #style =  models.ForeignKey('Style', on_delete=models.CASCADE, blank=True)
    create_date = models.DateField(editable=False, auto_now_add=True, blank=True)
    edit_date = models.DateField(editable=False, auto_now_add=True, blank=True)
    template = models.ForeignKey('Template', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Template(models.Model):
    name = models.CharField(max_length=64, blank=False)
    file = models.FileField(upload_to='uploads/') 

    def __str__(self):
        return self.name
