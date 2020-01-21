import datetime

from django.db import models

class TechField(models.Model):
    name = models.CharField(max_length=64, blank=False)
    
    def __str__(self):
        return self.name

class Tech(models.Model):
    name = models.CharField(max_length=64, default=None, blank=False)
    tech_field = models.ForeignKey(TechField, on_delete=models.CASCADE, related_name='tech', blank=True)

class Employee(models.Model):
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=128)
    phone = models.CharField(max_length=16)
    exposures = models.ManyToManyField(TechField, related_name='exposures', blank=True)

    def __str__(self):
        return self.name

class Duty(models.Model):
    description = models.CharField(max_length=256, default=None, blank=True)
   
    def __str__(self):
        return self.description

class Project(models.Model):
    description = models.CharField(max_length=256, default=None, blank=True)
    
    def __str__(self):
        return self.description


    def __str__(self):
        return self.name

class Employment(models.Model):
    company_name = models.CharField(max_length=128, default=None)
    job_title = models.CharField(max_length=64, default=None)
    start_date = models.DateField('Employement Start Date', default=None)
    end_date = models.DateField('Employement End Date', default=None)
    leave_reason = models.CharField(max_length=512, default=None)
    duties = models.ManyToManyField(Duty, related_name='duties')
    projects = models.ManyToManyField(Project, related_name='projects')

    def __str__(self):
        return self.company_name