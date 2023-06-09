from django.shortcuts import render

from .models import Nba_stats

def index(request):
    """The home page for stat_curry"""
    stats = Nba_stats.objects.all()
    return render(request, 'base/index.html', {'stats': stats})