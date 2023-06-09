"""Defines URL patterns for base."""

from django.urls import path

from . import views
from .views import index

app_name = 'base'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),

]