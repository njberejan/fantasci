from django import forms
from .models import LeagueRulesModel

class LeagueRulesForm(forms.ModelForm):
    class Meta:
        model = LeagueRulesModel
        fields = ('league_name', 'passing_yards_points', 'passing_yards_number_of_yards', 'passing_touchdowns',
        'interceptions', 'rushing_yards_points', 'rushing_yards_number_of_yards', 'rushing_touchdowns', 'receiving_yards_points',
        'receiving_yards_number_of_yards', 'receiving_touchdowns', 'fumble_recovered_for_td',
        'two_point_conversions', 'fumbles_lost', 'XP_made', 'FG_made', 'FG_long_made', 'sacks', 'd_interceptions',
        'fumbles_recovered', 'safeties', 'defensive_touchdowns', 'kick_punt_return_tds', 'points_allowed_value1',
        'points_allowed_value2', 'points_allowed_value3', 'points_allowed_value4', 'points_allowed_value5',
        'points_allowed_value6', 'points_allowed_value7',
        )
