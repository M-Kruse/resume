from django.contrib import admin

# Register your models here.
from .models import Employment, Employee, Duty, Project, Domain, Experience, Education, Reference

admin.site.register(Employee)
admin.site.register(Employment)
admin.site.register(Duty)
admin.site.register(Project)
admin.site.register(Domain)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Reference)

