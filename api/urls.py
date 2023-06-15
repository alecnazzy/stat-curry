from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='apiOverview'),
    path('players/<str:name>/', views.searchPlayer, name='searchPlayer'),
    path('players/', views.players, name='players'),
    path('teams/<str:team>/', views.searchTeam, name='searchTeam'),
    path('teams/', views.teams, name='teams'),
    path('leaders/', views.leaders, name='leaders'),
    path('leaders/points/', views.points, name='points'),
    path('leaders/assists/', views.assists, name='assists'),
    path('leaders/rebounds/', views.rebounds, name='rebounds'),
    path('leaders/steals/', views.steals, name='steals'),
    path('leaders/blocks/', views.blocks, name='blocks'),
    path('leaders/ft', views.ftAttempts, name='ftAttempts'),
    path('leaders/ft%', views.ftPercentage, name='ftPercentage'),
    path('leaders/twopoint', views.twoPointAttempts, name='twoPointAttempts'),
    path('leaders/twopoint%', views.twoPointPercentage, name='twoPointPercentage'),
    path('leaders/threepoint', views.threePointAttempts, name='threePointAttempts'),
    path('leaders/threepoint%', views.threePointPercentage, name='threePointPercentage'),
    path('leaders/efg%', views.efgPercentage, name='efgPercentage'),
    path('leaders/ts%', views.tsPercentage, name='tsPercentage'),
    path('leaders/offrating', views.offRating, name='offRating'),
    path('leaders/defrating', views.defRating, name='defRating'),
    path('leaders/turnovers', views.turnovers, name='turnovers'),
]