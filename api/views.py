from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Nba_stats
from .serializers import StatsSerializer

@api_view(['GET'])
def apiOverview(request):
    """Returns a list of all available endpoints"""
    api_urls = {
        'List of all players': '/players',
        'Search by player': '/players/Stephen Curry/',
        'List of all teams': '/teams', 
        'Search by team': '/teams/Golden State Warriors/',
        'Leaders by points': '/leaders/points',
        'Leaders by assists': '/leaders/assists',
        'Leaders by rebounds': '/leaders/rebounds',
        'Leaders by steals': '/leaders/steals',
        'Leaders by blocks': '/leaders/blocks',
        'Leaders by free throw attempts': '/leaders/ft',
        'Leaders by free throw percentage': '/leaders/ft%',
        'Leaders by two point attempts': '/leaders/twopoint',
        'Leaders by two point percentage': '/leaders/twopoint%',
        'Leaders by three point attempts': '/leaders/threepoint',
        'Leaders by three point percentage': '/leaders/threepoint%',
        'Leaders by effective field goal percentage': '/leaders/efg%',
        'Leaders by true shooting percentage': '/leaders/ts%',
        'Leaders by offensive rating': '/leaders/offrating',
        'Leaders by defensive rating': '/leaders/defrating',
        'Leaders by turnovers': '/leaders/turnovers',
    }
    return Response(api_urls)


# KEEP

@api_view(['GET'])
def searchPlayer(request, name):
    """Returns all stats in the database for a given player"""
    player = Nba_stats.objects.filter(name=name)
    serializer = StatsSerializer(player, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def players(request):
    """Returns all stats in the database for the 2022-23 NBA season"""
    players = Nba_stats.objects.order_by('name')
    serializer = StatsSerializer(players, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def searchTeam(request, team):
    """Returns all stats in the database for a given team"""
    team = Nba_stats.objects.filter(team=team)
    serializer = StatsSerializer(team, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def teams(request):
    """Returns all teams in the database"""
    teams = Nba_stats.objects.values_list('team', flat=True).distinct()
    return Response(teams)

@api_view(['GET'])
def leaders(request):
    """Returns all stats in the database sorted by rank"""
    leaders = Nba_stats.objects.order_by('rank')
    serializer = StatsSerializer(leaders, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def points(request):
    """Returns all stats in the database sorted by points per game"""
    points = Nba_stats.objects.order_by('ppg').reverse()
    serializer = StatsSerializer(points, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def assists(request):
    """Returns all stats in the database sorted by assists per game"""
    assists = Nba_stats.objects.order_by('apg').reverse()
    serializer = StatsSerializer(assists, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def rebounds(request):
    """Returns all stats in the database sorted by rebounds per game"""
    rebounds = Nba_stats.objects.order_by('rpg').reverse()
    serializer = StatsSerializer(rebounds, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def steals(request):
    """Returns all stats in the database sorted by steals per game"""
    steals = Nba_stats.objects.order_by('spg').reverse()
    serializer = StatsSerializer(steals, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def blocks(request):
    """Returns all stats in the database sorted by blocks per game"""
    blocks = Nba_stats.objects.order_by('bpg').reverse()
    serializer = StatsSerializer(blocks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ftAttempts(request):
    """Returns all stats in the database sorted by free throw percentage"""
    fta = Nba_stats.objects.order_by('ft_attempts').reverse()
    serializer = StatsSerializer(fta, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ftPercentage(request):
    """Returns all stats in the database sorted by free throw percentage"""
    ftp = Nba_stats.objects.order_by('ft_percent').reverse()
    serializer = StatsSerializer(ftp, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def threePointAttempts(request):
    """Returns all stats in the database sorted by three point attempts"""
    tpa = Nba_stats.objects.order_by('three_point_attempts').reverse()
    serializer = StatsSerializer(tpa, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def threePointPercentage(request):
    """Returns all stats in the database sorted by three point percentage"""
    tpp = Nba_stats.objects.order_by('three_point_percent').reverse()
    serializer = StatsSerializer(tpp, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def twoPointAttempts(request):
    """Returns all stats in the database sorted by two point attempts"""
    tpa = Nba_stats.objects.order_by('two_point_attempts').reverse()
    serializer = StatsSerializer(tpa, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def twoPointPercentage(request):
    """Returns all stats in the database sorted by two point percentage"""
    tpp = Nba_stats.objects.order_by('two_point_percent').reverse()
    serializer = StatsSerializer(tpp, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def efgPercentage(request):
    """Returns all stats in the database sorted by effective field goal percentage"""
    efg = Nba_stats.objects.order_by('efg_percent').reverse()
    serializer = StatsSerializer(efg, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def tsPercentage(request):
    """Returns all stats in the database sorted by true shooting percentage"""
    tsp = Nba_stats.objects.order_by('ts_percent').reverse().exclude(ts_percent=0)
    serializer = StatsSerializer(tsp, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def offRating(request):
    """Returns all stats in the database sorted by offensive rating"""
    off_rating = Nba_stats.objects.order_by('off_rating').reverse().exclude(off_rating=0)
    serializer = StatsSerializer(off_rating, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def defRating(request):
    """Returns all stats in the database sorted by defensive rating"""
    def_rating = Nba_stats.objects.order_by('def_rating').reverse().exclude(def_rating=0)
    serializer = StatsSerializer(def_rating, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def turnovers(request):
    """Returns all stats in the database sorted by turnovers per game"""
    tpg = Nba_stats.objects.order_by('tpg').reverse()
    serializer = StatsSerializer(tpg, many=True)
    return Response(serializer.data)
