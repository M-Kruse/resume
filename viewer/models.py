import datetime

from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=128)
    phone = models.CharField(max_length=16)

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

class TechField(models.Model):
    name = models.CharField(max_length=64)
    
    def __str__(self):
        return self.name

class Tech(models.Model):
    name = models.CharField(max_length=64, default=None, blank=True)
    tech_field = models.ManyToManyField(TechField)

    def __str__(self):
        return self.name

class Employment(models.Model):
    company_name = models.CharField(max_length=128, default=None)
    job_title = models.CharField(max_length=64, default=None)
    start_date = models.DateField('Employement Start Date', default=None)
    end_date = models.DateField('Employement End Date', default=None)
    leave_reason = models.CharField(max_length=512, default=None)
    duties = models.ManyToManyField(Duty)
    projects = models.ManyToManyField(Project)

    def __str__(self):
        return self.company_name