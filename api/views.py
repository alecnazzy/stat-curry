from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Nba_stats
from .serializers import StatsSerializer

@api_view(['GET'])
def apiOverview(request):
    """Returns a list of all available endpoints"""
    api_urls = {
        'List of all players': '/players/',
        'Search by player': '/players/Stephen Curry/',
        'List of all teams': '/teams/',
        'Search by team': '/teams/Golden State Warriors/',


        'Sort by Team': '/sortby/<str:team>/',
        'Sort by Team Scoring': '/sortby/<str:team>/scoring/',
        'Sort by Scoring': '/sortby/scoring/',
        'Sort by Assists': '/sortby/assists/',
        'Sort by Rebounds': '/sortby/rebounds/',
        'Sort by Steals': '/sortby/steals/',
        'Sort by Blocks': '/sortby/blocks/',
        'Sort by Position': '/sortby/<str:position>/',
        'Sort by Free Throw Attempts': '/sortby/ft/',
        'Sort by Free Throw Percentage': '/sortby/ft%',
        'Sort by Three Point Attempts': '/sortby/threepoint/',
        'Sort by Three Point Percentage': '/sortby/threepoint%',
        'Sort by Two Point Attempts': '/sortby/twopoint/',
        'Sort by Two Point Percentage': '/sortby/twopoint%',
        'Sort by Effective Field Goal Percentage': '/sortby/efg%',
        'Sort by True Shooting Percentage': '/sortby/ts%',
        'Sort by Offensive Rating': '/sortby/offrating/',
        'Sort by Defensive Rating': '/sortby/defrating/',
        'Sort by Turnovers Per Game': '/sortby/tpg/',
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
    players = Nba_stats.objects.order_by('rank')
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

# END KEEP




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
def searchByName(request, name):
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

@api_view(['GET'])
def sortByFreeThrowAttempts(request):
    """Returns all stats in the database sorted by free throw percentage"""
    fta = Nba_stats.objects.order_by('ft_attempts').reverse()
    serializer = StatsSerializer(fta, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def sortByFreeThrowPercentage(request):
    """Returns all stats in the database sorted by free throw percentage"""
    ftp = Nba_stats.objects.order_by('ft_percent').reverse()
    serializer = StatsSerializer(ftp, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def sortByThreePointAttempts(request):
    """Returns all stats in the database sorted by three point attempts"""
    tpa = Nba_stats.objects.order_by('three_point_attempts').reverse()
    serializer = StatsSerializer(tpa, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def sortByThreePointPercentage(request):
    """Returns all stats in the database sorted by three point percentage"""
    tpp = Nba_stats.objects.order_by('three_point_percent').reverse()
    serializer = StatsSerializer(tpp, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def sortByTwoPointAttempts(request):
    """Returns all stats in the database sorted by two point attempts"""
    tpa = Nba_stats.objects.order_by('two_point_attempts').reverse()
    serializer = StatsSerializer(tpa, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def sortByTwoPointPercentage(request):
    """Returns all stats in the database sorted by two point percentage"""
    tpp = Nba_stats.objects.order_by('two_point_percent').reverse()
    serializer = StatsSerializer(tpp, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def sortByEFGPercentage(request):
    """Returns all stats in the database sorted by effective field goal percentage"""
    efg = Nba_stats.objects.order_by('efg_percent').reverse()
    serializer = StatsSerializer(efg, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def sortByTSPercentage(request):
    """Returns all stats in the database sorted by true shooting percentage"""
    tsp = Nba_stats.objects.order_by('ts_percent').reverse().exclude(ts_percent=0)
    serializer = StatsSerializer(tsp, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def sortByOffRating(request):
    """Returns all stats in the database sorted by offensive rating"""
    off_rating = Nba_stats.objects.order_by('off_rating').reverse().exclude(off_rating=0)
    serializer = StatsSerializer(off_rating, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def sortByDefRating(request):
    """Returns all stats in the database sorted by defensive rating"""
    def_rating = Nba_stats.objects.order_by('def_rating').reverse().exclude(def_rating=0)
    serializer = StatsSerializer(def_rating, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def sortByTPG(request):
    """Returns all stats in the database sorted by turnovers per game"""
    tpg = Nba_stats.objects.order_by('tpg').reverse()
    serializer = StatsSerializer(tpg, many=True)
    return Response(serializer.data)
