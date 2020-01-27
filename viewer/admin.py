from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import Applicant, Employment, Duty, Project, Domain, Experience, Education, Reference

admin.site.register(Applicant)
admin.site.register(Employment)
admin.site.register(Duty)
admin.site.register(Project)
admin.site.register(Domain)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Reference)
