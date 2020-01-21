from django.contrib import admin

# Register your models here.
from .models import Employment, Duty, Project

admin.site.register(Employment)
admin.site.register(Duty)
admin.site.register(Project)