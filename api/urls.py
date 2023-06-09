from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='apiOverview'),
    path('stats/', views.stats, name='stats'),
    path('scoring/', views.sortByScoring, name='sortByScoring'),
    path('assists/', views.sortByAssists, name='sortByAssists'),
    path('rebounds/', views.sortByRebounds, name='sortByRebounds'),
    path('steals/', views.sortBySteals, name='sortBySteals'),
    path('blocks/', views.sortByBlocks, name='sortByBlocks'),
    path('team/<str:team>/', views.sortByTeam, name='sortByTeam'),
    path('player/<str:name>/', views.sortByName, name='sortByName'),
    path('position/<str:position>/', views.sortByPosition, name='sortByPosition'),
    path('team/<str:team>/scoring/', views.sortByTeamScoring, name='sortByTeamScoring'),
]