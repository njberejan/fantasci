class AveragePlayer:

    def __init__(self, player_list):
        self.avg_rush_attempts = self.calculate(player.rush_attempts)
        self.avg_rush_yards = round(((sum(player.rush_yards for player in player_list if player.rush_yards != None))/len(player_list)),1)
        self.avg_rush_touchdowns = round(((sum(player.rush_touchdowns for player in player_list if player.rush_touchdowns != None))/len(player_list)),1)
        self.avg_rush_long = round(((sum(player.rush_long for player in player_list if player.rush_long != None))/len(player_list)),1)
        self.avg_rush_long_touchdown = round(((sum(player.rush_long_touchdown for player in player_list if player.rush_long_touchdown != None))/len(player_list)),1)
        self.avg_rush_two_point_attempt = round(((sum(player.rush_two_point_attempt for player in player_list if player.rush_two_point_attempt != None))/len(player_list)),1)
        self.avg_rush_two_point_makes = round(((sum(player.rush_two_point_makes for player in player_list if player.rush_two_point_makes!= None))/len(player_list)),1)
        self.avg_receptions = round(((sum(player.receptions for player in player_list if player.receptions != None))/len(player_list)),1)
        self.avg_receiving_yards = round(((sum(player.receiving_yards for player in player_list if player.receiving_yards != None))/len(player_list)),1)
        self.avg_receiving_touchdowns = round(((sum(player.receiving_touchdowns for player in player_list if player.receiving_touchdowns != None))/len(player_list)),1)
        self.avg_receiving_long = round(((sum(player.receiving_long for player in player_list if player.receiving_long != None))/len(player_list)),1)
        self.avg_receiving_long_touchdown = round(((sum(player.receiving_long_touchdown for player in player_list if player.receiving_long_touchdown != None))/len(player_list)),1)
        self.avg_receiving_two_point_attempts = round(((sum(player.receiving_two_point_attempts for player in player_list if player.receiving_two_point_attempts != None))/len(player_list)),1)
        self.avg_receiving_two_point_makes = round(((sum(player.receiving_two_point_makes for player in player_list if player.receiving_two_point_makes != None))/len(player_list)),1)
        self.avg_passing_attempts = round(((sum(player.passing_attempts for player in player_list if player.passing_attempts != None))/len(player_list)),1)
        self.avg_passing_completions = round(((sum(player.passing_completions for player in player_list if player.passing_completions != None))/len(player_list)),1)
        self.avg_passing_yards = round(((sum(player.passing_yards for player in player_list if player.passing_yards != None))/len(player_list)),1)
        self.avg_passing_touchdowns = round(((sum(player.passing_touchdowns for player in player_list if player.passing_touchdowns != None))/len(player_list)),1)
        self.avg_passing_interceptions = round(((sum(player.passing_interceptions for player in player_list if player.passing_interceptions != None))/len(player_list)),1)
        self.avg_passing_two_point_attempts = round(((sum(player.passing_two_point_attempts for player in player_list if player.passing_two_point_attempts != None))/len(player_list)),1)
        self.avg_passing_two_point_makes = round(((sum(player.passing_two_point_makes for player in player_list if player.passing_two_point_makes != None))/len(player_list)),1)
        self.avg_total_fumbles = round(((sum(player.total_fumbles for player in player_list if player.total_fumbles != None))/len(player_list)),1)
        self.avg_recovered_fumbles = round(((sum(player.recovered_fumbles for player in player_list if player.recovered_fumbles != None))/len(player_list)),1)
        self.avg_team_recovered_fumbles = round(((sum(player.team_recovered_fumbles for player in player_list if player.team_recovered_fumbles != None))/len(player_list)),1)
        self.avg_fumble_yards = round(((sum(player.fumble_yards for player in player_list if player.fumble_yards != None))/len(player_list)),1)
        self.avg_fumbles_lost = round(((sum(player.fumbles_lost for player in player_list if player.fumbles_lost != None))/len(player_list)),1)

    def calculate(STDIN):
        return round(((sum(STDIN for player in player_list if player.rush_attempts != None))/len(player_list)),1)
        """Do this for all class attributes on page"""

class AverageKicker:

    def __init__(self, player_list):
        self.avg_attempts = round(((sum(player.attempts for player in player_list if player.attempts != None))/len(player_list)),1)
        self.avg_made = round(((sum(player.made for player in player_list if player.made != None))/len(player_list)),1)
        self.avg_yards = round(((sum(player.yards for player in player_list if player.yards != None))/len(player_list)),1)
        self.avg_percent = round(((sum(player.percent for player in player_list if player.percent != None))/len(player_list)),1)
        self.avg_xp_attempt = round(((sum(player.xp_attempt for player in player_list if player.xp_attempt != None))/len(player_list)),1)
        self.avg_xp_made = round(((sum(player.xp_made for player in player_list if player.xp_made != None))/len(player_list)),1)
        self.avg_xp_missed = round(((sum(player.xp_missed for player in player_list if player.xp_missed != None))/len(player_list)),1)
        self.avg_xp_blocked = round(((sum(player.xp_blocked for player in player_list if player.xp_blocked != None))/len(player_list)),1)
        self.avg_xp_total = round(((sum(player.xp_total for player in player_list if player.xp_total != None))/len(player_list)),1)

class AverageDefense:

    def __init__(self, player_list):
        """defense"""
        self.avg_tackles = round(((sum(player.tackles for player in player_list if player.tackles != None))/len(player_list)),1)
        self.avg_assisted_tackles = round(((sum(player.assisted_tackles for player in player_list if player.assisted_tackles != None))/len(player_list)),1)
        self.avg_sacks = round(((sum(player.sacks for player in player_list if player.sacks != None))/len(player_list)),1)
        self.avg_interceptions = round(((sum(player.interceptions for player in player_list if player.interceptions != None))/len(player_list)),1)
        self.avg_forced_fumbles = round(((sum(player.forced_fumbles for player in player_list if player.forced_fumbles != None))/len(player_list)),1)
        self.avg_first_downs_allowed = round(((sum(player.first_downs_allowed for player in player_list if player.first_downs_allowed != None))/len(player_list)),1)
        self.avg_total_yards_allowed = round(((sum(player.total_yards_allowed for player in player_list if player.total_yards_allowed != None))/len(player_list)),1)
        self.avg_passing_yards_allowed = round(((sum(player.passing_yards_allowed for player in player_list if player.passing_yards_allowed != None))/len(player_list)),1)
        self.avg_rushing_yards_allowed = round(((sum(player.rushing_yards_allowed for player in player_list if player.rushing_yards_allowed != None))/len(player_list)),1)
        self.avg_penalties = round(((sum(player.penalties for player in player_list if player.penalties != None))/len(player_list)),1)
        self.avg_penalty_yards = round(((sum(player.penalty_yards for player in player_list if player.penalty_yards != None))/len(player_list)),1)
        self.avg_turnovers = round(((sum(player.turnovers for player in player_list if player.turnovers != None))/len(player_list)),1)
        self.avg_total_punts = round(((sum(player.total_punts for player in player_list if player.total_punts != None))/len(player_list)),1)
        self.avg_punt_yards = round(((sum(player.punt_yards for player in player_list if player.punt_yards != None))/len(player_list)),1)
        self.avg_punt_yards_average = round(((sum(player.punt_yards_average for player in player_list if player.punt_yards_average != None))/len(player_list)),1)
        """ST"""
        self.avg_xp_attempt = round(((sum(player.xp_attempt for player in player_list if player.xp_attempt != None))/len(player_list)),1)
        self.avg_kicking_yards = round(((sum(player.kicking_yards for player in player_list if player.kicking_yards != None))/len(player_list)),1)
        self.avg_kicking_attempts = round(((sum(player.kicking_attempts for player in player_list if player.kicking_attempts != None))/len(player_list)),1)
        self.avg_xp_missed = round(((sum(player.xp_missed for player in player_list if player.xp_missed != None))/len(player_list)),1)
        self.avg_kicks_made = round(((sum(player.kicks_made for player in player_list if player.kicks_made != None))/len(player_list)),1)
        self.avg_xp_made = round(((sum(player.xp_made for player in player_list if player.xp_made != None))/len(player_list)),1)
        self.avg_xp_blocked = round(((sum(player.xp_blocked for player in player_list if player.xp_blocked != None))/len(player_list)),1)
        self.avg_xp_total = round(((sum(player.xp_total for player in player_list if player.xp_total != None))/len(player_list)),1)
        self.avg_kick_returns = round(((sum(player.kick_returns for player in player_list if player.kick_returns != None))/len(player_list)),1)
        self.avg_kick_returns_long = round(((sum(player.kick_returns_long for player in player_list if player.kick_returns_long != None))/len(player_list)),1)
        self.avg_kick_returns_long_touchdown = round(((sum(player.kick_returns_long_touchdown for player in player_list if player.kick_returns_long_touchdown != None))/len(player_list)),1)
        self.avg_kick_returns_touchdowns = round(((sum(player.kick_returns_touchdowns for player in player_list if player.kick_returns_touchdowns != None))/len(player_list)),1)
        self.avg_punt_returns = round(((sum(player.punt_returns for player in player_list if player.punt_returns != None))/len(player_list)),1)
        self.avg_punt_returns_long = round(((sum(player.punt_returns_long for player in player_list if player.punt_returns_long != None))/len(player_list)),1)
        self.avg_punt_returns_long_touchdown = round(((sum(player.punt_returns_long_touchdown for player in player_list if player.punt_returns_long_touchdowns != None))/len(player_list)),1)
        self.avg_punt_returns_touchdowns = round(((sum(player.punt_returns_touchdowns for player in player_list if player.punt_returns_touchdowns != None))/len(player_list)),1)
