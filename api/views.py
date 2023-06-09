from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Nba_stats
from .serializers import StatsSerializer

@api_view(['GET'])
def apiOverview(request):
    """Returns a list of all available endpoints"""
    api_urls = {
        'Stats': '/stats/',
        'Sort by Scoring': '/scoring/',
        'Sort by Assists': '/assists/',
        'Sort by Rebounds': '/rebounds/',
        'Sort by Steals': '/steals/',
        'Sort by Blocks': '/blocks/',
        'Sort by Team': '/team/<str:team>/',
        'Sort by Player': '/player/<str:name>/',
        'Sort by Position': '/position/<str:position>/',
        'Sort by Team Scoring': '/team/<str:team>/scoring/'
    }
    return Response(api_urls)

@api_view(['GET'])
def stats(request):
    """Returns all stats in the database for the 2022-23 NBA season"""
    stats = Nba_stats.objects.all()
    serializer = StatsSerializer(stats, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def sortByScoring(request):
    """Returns all stats in the database sorted by points per game"""
    scoring = Nba_stats.objects.order_by('ppg').reverse()
    serializer = StatsSerializer(scoring, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def sortByAssists(request):
    """Returns all stats in the database sorted by assists per game"""
    assists = Nba_stats.objects.order_by('apg').reverse()
    serializer = StatsSerializer(assists, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def sortByRebounds(request):
    """Returns all stats in the database sorted by rebounds per game"""
    rebounds = Nba_stats.objects.order_by('rpg').reverse()
    serializer = StatsSerializer(rebounds, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def sortBySteals(request):
    """Returns all stats in the database sorted by steals per game"""
    steals = Nba_stats.objects.order_by('spg').reverse()
    serializer = StatsSerializer(steals, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def sortByBlocks(request):
    """Returns all stats in the database sorted by blocks per game"""
    blocks = Nba_stats.objects.order_by('bpg').reverse()
    serializer = StatsSerializer(blocks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def sortByTeam(request, team):
    """Returns all stats in the database for a given team"""
    team = Nba_stats.objects.filter(team=team)
    serializer = StatsSerializer(team, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def sortByName(request, name):
    """Returns all stats in the database for a given player"""
    name = Nba_stats.objects.filter(name=name)
    serializer = StatsSerializer(name, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def sortByPosition(request, position):
    """Returns all stats in the database for a given position"""
    position = Nba_stats.objects.filter(pos=position)
    serializer = StatsSerializer(position, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def sortByTeamScoring(request, team):
    """Returns all stats in the database for a given team sorted by points per game"""
    scoring = Nba_stats.objects.filter(team=team).order_by('ppg').reverse()
    serializer = StatsSerializer(scoring, many=True)
    return Response(serializer.data)
