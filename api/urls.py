from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='apiOverview'),
    path('players/<str:name>/', views.searchPlayer, name='searchPlayer'),
    path('players/', views.players, name='players'),
    path('teams/<str:team>/', views.searchTeam, name='searchTeam'),
    path('teams/', views.teams, name='teams'),

    path('sortby/scoring/', views.sortByScoring, name='sortByScoring'),
    path('sortby/assists/', views.sortByAssists, name='sortByAssists'),
    path('sortby/rebounds/', views.sortByRebounds, name='sortByRebounds'),
    path('sortby/steals/', views.sortBySteals, name='sortBySteals'),
    path('sortby/blocks/', views.sortByBlocks, name='sortByBlocks'),
    path('sortby/<str:team>/', views.sortByTeam, name='sortByTeam'),
    path('stats/<str:name>/', views.searchByName, name='searchByName'),
    path('sortby/<str:position>/', views.sortByPosition, name='sortByPosition'),
    path('sortby/<str:team>/scoring/', views.sortByTeamScoring, name='sortByTeamScoring'),
    path('sortby/ft', views.sortByFreeThrowAttempts, name='sortByFreeThrowAttempts'),
    path('sortby/ft%', views.sortByFreeThrowPercentage, name='sortByFreeThrowPercentage'),
    path('sortby/threepoint', views.sortByThreePointAttempts, name='sortByThreePointAttempts'),
    path('sortby/threepoint%', views.sortByThreePointPercentage, name='sortByThreePointPercentage'),
    path('sortby/twopoint', views.sortByTwoPointAttempts, name='sortByTwoPointAttempts'),
    path('sortby/twopoint%', views.sortByTwoPointPercentage, name='sortByTwoPointPercentage'),
    path('sortby/efg%', views.sortByEFGPercentage, name='sortByEFGPercentage'),
    path('sortby/ts%', views.sortByTSPercentage, name='sortByTSPercentage'),
    path('sortby/offrating', views.sortByOffRating, name='sortByOffRating'),
    path('sortby/defrating', views.sortByDefRating, name='sortByDefRating'),
    path('sortby/tpg', views.sortByTPG, name='sortByTPG'),
]