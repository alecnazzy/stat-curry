from django.db import models

class Nba_stats(models.Model):
    rank = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    pos = models.CharField(max_length=100)
    age = models.IntegerField()
    games_played = models.IntegerField()
    min_per_game = models.FloatField()
    ft_attempts = models.FloatField()
    ft_percent = models.FloatField()
    two_point_attempts = models.FloatField()
    two_point_percent = models.FloatField()
    three_point_attempts = models.FloatField()
    three_point_percent = models.FloatField()
    efg_percent = models.FloatField()
    ts_percent = models.FloatField()
    ppg = models.FloatField()
    rpg = models.FloatField()
    apg = models.FloatField()
    spg = models.FloatField()
    bpg = models.FloatField()
    tpg = models.FloatField()
    off_rating = models.FloatField()
    def_rating = models.FloatField()

    def __str__(self):
        return f"rank: {self.rank} | name: {self.name} | team: {self.team} | pos: {self.pos} | age:{self.age} | gp: {self.games_played} | mpg: {self.min_per_game} | fta: {self.ft_attempts} | ft%: {self.ft_percent} | 2pa: {self.two_point_attempts} | 2p%: {self.two_point_percent} | 3pa: {self.three_point_attempts} | 3p%: {self.three_point_percent} | efg%: {self.efg_percent} | ts%: {self.ts_percent} | ppg: {self.ppg} | rpg: {self.rpg} | apg: {self.apg} | spg: {self.spg} | bpg: {self.bpg} | tpg: {self.tpg} | offensive rating: {self.off_rating} | defensive rating: {self.def_rating}"
        