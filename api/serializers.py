from rest_framework import serializers
from base.models import Nba_stats

class StatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nba_stats
        fields = '__all__'