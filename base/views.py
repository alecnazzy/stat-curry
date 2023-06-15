from django.shortcuts import render

from .models import Nba_stats

def index(request):
    """The home page for stat_curry"""
    return render(request, 'base/index.html')

def docs(request):
    """The docs page for NBAPI"""
    return render(request, 'base/docs.html')
