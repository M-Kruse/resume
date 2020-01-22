from django.contrib import admin

# Register your models here.
from .models import Employment, Employee, Duty, Project, TechField, Tech, Education, Reference

admin.site.register(Employee)
admin.site.register(Employment)
admin.site.register(Duty)
admin.site.register(Project)
admin.site.register(TechField)
admin.site.register(Tech)
admin.site.register(Education)
admin.site.register(Reference)

