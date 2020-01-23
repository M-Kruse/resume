from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'resume'
urlpatterns = [
	path('', views.IndexView.as_view(), name="index"),
    path('html/', views.HTMLView.as_view(), name="html"),
]