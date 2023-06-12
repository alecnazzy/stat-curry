from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='apiOverview'),
    path('stats/', views.stats, name='stats'),
    path('sortby/scoring/', views.sortByScoring, name='sortByScoring'),
    path('sortby/assists/', views.sortByAssists, name='sortByAssists'),
    path('sortby/rebounds/', views.sortByRebounds, name='sortByRebounds'),
    path('sortby/steals/', views.sortBySteals, name='sortBySteals'),
    path('sortby/blocks/', views.sortByBlocks, name='sortByBlocks'),
    path('sortby/<str:team>/', views.sortByTeam, name='sortByTeam'),
    path('stats/<str:name>/', views.searchByName, name='searchByName'),
    path('sortby/<str:position>/', views.sortByPosition, name='sortByPosition'),
    path('sortby/<str:team>/scoring/', views.sortByTeamScoring, name='sortByTeamScoring'),
]