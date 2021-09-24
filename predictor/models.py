from django.db import models
from django.contrib.auth.models import User

class PlayerModel(models.Model):

    name = models.CharField(max_length=100)
    game = models.CharField(max_length=100, default=None, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    rush_attempts = models.CharField(max_length=100, default=None, null=True)
    rush_yards = models.CharField(max_length=100, default=None, null=True)
    rush_touchdowns = models.CharField(max_length=100, default=None, null=True)
    rush_long = models.CharField(max_length=100, default=None, null=True)
    rush_long_touchdown = models.CharField(max_length=100, default=None, null=True)
    rush_two_point_attempt = models.CharField(max_length=100, default=None, null=True)
    rush_two_point_makes = models.CharField(max_length=100, default=None, null=True)

    receptions = models.CharField(max_length=100, default=None, null=True)
    receiving_yards = models.CharField(max_length=100, default=None, null=True)
    receiving_touchdowns = models.CharField(max_length=100, default=None, null=True)
    receiving_long = models.CharField(max_length=100, default=None, null=True)
    receiving_long_touchdown = models.CharField(max_length=100, default=None, null=True)
    receiving_two_point_attempts = models.CharField(max_length=100, default=None, null=True)
    receiving_two_point_makes = models.CharField(max_length=100, default=None, null=True)

    passing_attempts = models.CharField(max_length=100, default=None, null=True)
    passing_completions = models.CharField(max_length=100, default=None, null=True)
    passing_yards = models.CharField(max_length=100, default=None, null=True)
    passing_touchdowns = models.CharField(max_length=100, default=None, null=True)
    passing_interceptions = models.CharField(max_length=100, default=None, null=True)
    passing_two_point_attempts = models.CharField(max_length=100, default=None, null=True)
    passing_two_point_makes = models.CharField(max_length=100, default=None, null=True)

    total_fumbles = models.CharField(max_length=100, default=None, null=True)
    recovered_fumbles = models.CharField(max_length=100, default=None, null=True)
    team_recovered_fumbles = models.CharField(max_length=100, default=None, null=True)
    fumble_yards = models.CharField(max_length=100, default=None, null=True)
    fumbles_lost = models.CharField(max_length=100, default=None, null=True)

class KickerModel(models.Model):

    name = models.CharField(max_length=100, default=None, null=True)
    game = models.CharField(max_length=100, default=None, null=True)
    attempts = models.CharField(max_length=100, default=None, null=True)
    made = models.CharField(max_length=100, default=None, null=True)
    yards = models.CharField(max_length=100, default=None, null=True)
    percent = models.CharField(max_length=100, default=None, null=True)
    xp_attempt = models.CharField(max_length=100, default=None, null=True)
    xp_made = models.CharField(max_length=100, default=None, null=True)
    xp_missed = models.CharField(max_length=100, default=None, null=True)
    xp_blocked = models.CharField(max_length=100, default=None, null=True)
    xp_total = models.CharField(max_length=100, default=None, null=True)

class DefenseModel(models.Model):
    """must aggregate via method"""
    tackles = models.CharField(max_length=100, default=None, null=True)
    assisted_tackles = models.CharField(max_length=100, default=None, null=True)
    sacks = models.CharField(max_length=100, default=None, null=True)
    interceptions = models.CharField(max_length=100, default=None, null=True)
    forced_fumbles = models.CharField(max_length=100, default=None, null=True)
    """must aggregate via ST method"""
    xp_attempt = models.CharField(max_length=100, default=None, null=True)
    kicking_yards = models.CharField(max_length=100, default=None, null=True)
    kicking_attempts = models.CharField(max_length=100, default=None, null=True)
    xp_missed = models.CharField(max_length=100, default=None, null=True)
    kicks_made = models.CharField(max_length=100, default=None, null=True)
    xp_made = models.CharField(max_length=100, default=None, null=True)
    xp_blocked = models.CharField(max_length=100, default=None, null=True)
    xp_total = models.CharField(max_length=100, default=None, null=True)
    kick_returns = models.CharField(max_length=100, default=None, null=True)
    kick_returns_long = models.CharField(max_length=100, default=None, null=True)
    kick_returns_long_touchdown = models.CharField(max_length=100, default=None, null=True)
    kick_returns_touchdowns = models.CharField(max_length=100, default=None, null=True)
    punt_returns = models.CharField(max_length=100, default=None, null=True)
    punt_returns_long = models.CharField(max_length=100, default=None, null=True)
    punt_returns_long_touchdown = models.CharField(max_length=100, default=None, null=True)
    punt_returns_touchdowns = models.CharField(max_length=100, default=None, null=True)
    """retrieve straight from the API per week"""
    team = models.CharField(max_length=100)
    nfl_game_id = models.CharField(max_length=100, default=None, null=True)
    home_or_away = models.CharField(max_length=100, default=None, null=True)
    points_allowed = models.CharField(max_length=100, default=None, null=True)
    opponent = models.CharField(max_length=100, default=None, null=True)
    first_downs_allowed = models.CharField(max_length=100, default=None, null=True)
    total_yards_allowed = models.CharField(max_length=100, default=None, null=True)
    passing_yards_allowed = models.CharField(max_length=100, default=None, null=True)
    rushing_yards_allowed = models.CharField(max_length=100, default=None, null=True)
    penalties = models.CharField(max_length=100, default=None, null=True)
    penalty_yards = models.CharField(max_length=100, default=None, null=True)
    turnovers = models.CharField(max_length=100, default=None, null=True)
    total_punts = models.CharField(max_length=100, default=None, null=True)
    punt_yards = models.CharField(max_length=100, default=None, null=True)
    punt_yards_average = models.CharField(max_length=100, default=None, null=True)

class LeagueRulesModel(models.Model):
    league_name = models.CharField(max_length=50, default="My League")
    """model for league settings tied to user account, for use in calculating predicted scores"""
    owner = models.ForeignKey(User)

    """offense"""
    passing_yards_points = models.FloatField(default=1, null=True)
    passing_yards_number_of_yards = models.FloatField(default=25, null=True)
    """x points per y yards"""
    passing_touchdowns = models.FloatField(default=6, null=True)
    interceptions = models.FloatField(default=-2, null=True)

    rushing_yards_points = models.FloatField(default=1, null=True)
    rushing_yards_number_of_yards = models.FloatField(default=10, null=True)
    """x points per y yards"""
    rushing_touchdowns = models.FloatField(default=6, null=True)

    receiving_yards_points = models.FloatField(default=1, null=True)
    receiving_yards_number_of_yards = models.FloatField(default=10, null=True)
    receiving_touchdowns = models.FloatField(default=6, null=True)

    fumble_recovered_for_td = models.FloatField(default=6, null=True)
    two_point_conversions = models.FloatField(default=2, null=True)
    fumbles_lost = models.FloatField(default=-2, null=True)

    """kicking (FG_long >= 50 yds)"""
    XP_made = models.FloatField(default=1, null=True)
    FG_made = models.FloatField(default=3, null=True)
    FG_long_made = models.FloatField(default=5, null=True)

    """defense/st"""
    sacks = models.FloatField(default=1, null=True)
    d_interceptions = models.FloatField(default=2, null=True)
    fumbles_recovered = models.FloatField(default=2, null=True)
    safeties = models.FloatField(default=2, null=True)
    defensive_touchdowns = models.FloatField(default=6, null=True)
    kick_punt_return_tds = models.FloatField(default=6, null=True)
    points_allowed_value1 = models.FloatField(default=5, null=True)
    """0 points allowed"""
    points_allowed_value2 = models.FloatField(default=4, null=True)
    """1-6 points allowed"""
    points_allowed_value3 = models.FloatField(default=3, null=True)
    """7-13 points allowed"""
    points_allowed_value4 = models.FloatField(default=1, null=True)
    """14-20-6 points allowed"""
    points_allowed_value5 = models.FloatField(default=0, null=True)
    """21-27 points allowed"""
    points_allowed_value6 = models.FloatField(default=-3, null=True)
    """28-34 points allowed"""
    points_allowed_value7 = models.FloatField(default=-5, null=True)
    """35+ points allowed"""

    """Points Allowed (0): 10 points
    Points Allowed (1-6): 7 points
    Points Allowed (7-13): 4 points
    Points Allowed (14-20): 1 points
    Points Allowed (21-27): 0 points
    Points Allowed (28-34): -1 points
    Points Allowed (35+): -4 points"""

    def calc_QB_score(self, values):
        pass_td_score = values[0] * self.passing_touchdowns
        pass_yd_score = values[1] * (self.passing_yards_points/self.passing_yards_number_of_yards)
        rush_td_score = values[2] * self.rushing_touchdowns
        rush_yd_score = values[3] * (self.rushing_yards_points/self.rushing_yards_number_of_yards)
        total_score = pass_td_score + pass_yd_score + rush_td_score + rush_yd_score
        return total_score

    """if RB or WR or TE"""
    def calc_RB_or_WR_or_TE_score(self, values):
        rush_td_score = values[0] * self.rushing_touchdowns
        rush_yd_score = values[1] * (self.rushing_yards_points/self.rushing_yards_number_of_yards)
        rec_td_score = values[2] * self.receiving_touchdowns
        rec_yd_score = values[3] * (self.receiving_yards_points/self.receiving_yards_number_of_yards)
        total_score = rush_td_score + rush_yd_score + rec_td_score + rec_yd_score
        return total_score

    """if K"""
    def calc_K_score(self, values):
        kicks_made_score = values[0] * self.FG_made
        # kick_yards_score = values[1] * self.yards
        xp_made_score = values[2] * self.XP_made
        #need FG long made?
        total_score = kicks_made_score + xp_made_score
        return total_score



"""local lookup, if he is not in database, grab him from API."""

"""created and updated field on player model"""
