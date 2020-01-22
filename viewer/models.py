import datetime

from django.db import models

class Employment(models.Model):
    company_name = models.CharField(max_length=128, default=None)
    job_title = models.CharField(max_length=64, default=None)
    start_date = models.DateField('Employement Start Date', default=None)
    end_date = models.DateField('Employement End Date', default=None)
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

class Employee(models.Model):
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=128)
    phone = models.CharField(max_length=16)
    exposures = models.ManyToManyField('TechField', related_name='exposures', blank=True)
    education = models.ManyToManyField('Education', related_name='education', blank=True)
    references = models.ManyToManyField('Reference', related_name='references', blank=True)

    def __str__(self):
        return self.name

class TechField(models.Model):
    name = models.CharField(max_length=64, blank=False)
    techs = models.ManyToManyField('Tech', related_name='techs', blank=True)

    def __str__(self):
        return self.name

class Tech(models.Model):
    name = models.CharField(max_length=64, default=None, blank=False)

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
    employment = models.ManyToManyField('Employment', related_name='employment', blank=True)
    
    def __str__(self):
        return self.name
