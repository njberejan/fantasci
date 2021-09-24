import requests
import json

class Player:

    def __init__(self, dictionary, game):
        self.game = game

        for key, value in dictionary.items():
            self.name = dictionary[key]['name']

        if dictionary.get('rushing') is None:

            self.rush_attempts = 0
            self.rush_yards = 0
            self.rush_touchdowns = 0
            self.rush_long = 0
            self.rush_long_touchdown = 0
            self.rush_two_point_attempt = 0
            self.rush_two_point_makes = 0

        if dictionary.get('receiving') is None:

            self.receptions = 0
            self.receiving_yards = 0
            self.receiving_touchdowns = 0
            self.receiving_long = 0
            self.receiving_long_touchdown = 0
            self.receiving_two_point_attempts = 0
            self.receiving_two_point_makes = 0

        if dictionary.get('passing') is None:

            self.passing_attempts = 0
            self.passing_completions = 0
            self.passing_yards = 0
            self.passing_touchdowns = 0
            self.passing_interceptions = 0
            self.passing_two_point_attempts = 0
            self.passing_two_point_makes = 0

        if dictionary.get('fumbles') is None:

            self.total_fumbles = 0
            self.recovered_fumbles = 0
            self.team_recovered_fumbles = 0
            self.fumble_yards = 0
            self.fumbles_lost = 0

        for key, value in dictionary.items():

            if key == 'rushing':

                self.rush_attempts = dictionary[key].get('attempts', 0)
                self.rush_yards = dictionary[key].get('yards', 0)
                self.rush_touchdowns = dictionary.get('touchdowns', 0)
                self.rush_long = dictionary[key].get('long', 0)
                self.rush_long_touchdown = dictionary[key].get('long_touchdown', 0)
                self.rush_two_point_attempt = dictionary[key].get('two_point_attempts', 0)
                self.rush_two_point_makes = dictionary[key].get('two_point_makes', 0)

            if key == 'receiving':

                self.receptions = dictionary[key].get('receptions', 0)
                self.receiving_yards = dictionary[key].get('yards', 0)
                self.receiving_touchdowns = dictionary[key].get('touchdowns', 0)
                self.receiving_long = dictionary[key].get('long', 0)
                self.receiving_long_touchdown = dictionary[key].get('long_touchdown', 0)
                self.receiving_two_point_attempts = dictionary[key].get('two_point_attempts', 0)
                self.receiving_two_point_makes = dictionary[key].get('two_point_makes', 0)

            if key == 'passing':

                self.passing_attempts = dictionary[key].get('attempts', 0)
                self.passing_completions = dictionary[key].get('completions', 0)
                self.passing_yards = dictionary[key].get('yards', 0)
                self.passing_touchdowns = dictionary[key].get('touchdowns', 0)
                self.passing_interceptions = dictionary[key].get('interceptions', 0)
                self.passing_two_point_attempts = dictionary[key].get('two_point_attempts', 0)
                self.passing_two_point_makes = dictionary[key].get('two_point_makes', 0)


            if key == 'fumbles':

                self.total_fumbles = dictionary[key].get('total_fumbles', 0)
                self.recovered_fumbles = dictionary[key].get('recovered_fumbles', 0)
                self.team_recovered_fumbles = dictionary[key].get('team_recovered', 0)
                self.fumble_yards = dictionary[key].get('yards', 0)
                self.fumbles_lost = dictionary[key].get('fumbles_lost', 0)

# class Player:
  """old code see above for refactored 9/15/16 """
#     def __init__(self, dictionary, game):
#         self.game = game
#         try:
#             self.name = dictionary['passing']['name']
#         except KeyError:
#             try:
#                 self.name = dictionary['rushing']['name']
#             except KeyError:
#                 try:
#                     self.name = dictionary['receiving']['name']
#                 except KeyError:
#                     self.name = dictionary['fumbles']['name']
#
#         try:
#             self.rush_attempts = dictionary['rushing']['attempts']
#             self.rush_yards = dictionary['rushing']['yards']
#             self.rush_touchdowns = dictionary['rushing']['touchdowns']
#             self.rush_long = dictionary['rushing']['long']
#             self.rush_long_touchdown = dictionary['rushing']['long_touchdown']
#             self.rush_two_point_attempt = dictionary['rushing']['two_point_attempts']
#             self.rush_two_point_makes = dictionary['rushing']['two_point_makes']
#
#         except KeyError:
#             self.rush_attempts = 0
#             self.rush_yards = 0
#             self.rush_touchdowns = 0
#             self.rush_long = 0
#             self.rush_long_touchdown = 0
#             self.rush_two_point_attempt = 0
#             self.rush_two_point_makes = 0
#
#         try:
#             self.receptions = dictionary['receiving']['receptions']
#             self.receiving_yards = dictionary['receiving']['yards']
#             self.receiving_touchdowns = dictionary['receiving']['touchdowns']
#             self.receiving_long = dictionary['receiving']['long']
#             self.receiving_long_touchdown = dictionary['receiving']['long_touchdown']
#             self.receiving_two_point_attempts = dictionary['receiving']['two_point_attempts']
#             self.receiving_two_point_makes = dictionary['receiving']['two_point_makes']
#
#         except KeyError:
#             self.receptions = 0
#             self.receiving_yards = 0
#             self.receiving_touchdowns = 0
#             self.receiving_long = 0
#             self.receiving_long_touchdown = 0
#             self.receiving_two_point_attempts = 0
#             self.receiving_two_point_makes = 0
#
#         try:
#             self.passing_attempts = dictionary['passing']['attempts']
#             self.passing_completions = dictionary['passing']['completions']
#             self.passing_yards = dictionary['passing']['yards']
#             self.passing_touchdowns = dictionary['passing']['touchdowns']
#             self.passing_interceptions = dictionary['passing']['interceptions']
#             self.passing_two_point_attempts = dictionary['passing']['two_point_attempts']
#             self.passing_two_point_makes = dictionary['passing']['two_point_makes']
#
#         except KeyError:
#             self.passing_attempts = 0
#             self.passing_completions = 0
#             self.passing_yards = 0
#             self.passing_touchdowns = 0
#             self.passing_interceptions = 0
#             self.passing_two_point_attempts = 0
#             self.passing_two_point_makes = 0
#
#         try:
#             self.total_fumbles = dictionary['fumbles']['total_fumbles']
#             self.recovered_fumbles = dictionary['fumbles']['recovered']
#             self.team_recovered_fumbles = dictionary['fumbles']['team_recovered']
#             self.fumble_yards = dictionary['fumbles']['yards']
#             self.fumbles_lost = dictionary['fumbles']['fumbles_lost']
#
#         except KeyError:
#             self.total_fumbles = 0
#             self.recovered_fumbles = 0
#             self.team_recovered_fumbles = 0
#             self.fumble_yards = 0
#             self.fumbles_lost = 0

class Kicker:

    def __init__(self, dictionary, game):
        self.game = game
        self.name = dictionary['kicking']['name']
        self.attempts = dictionary['kicking']['attempts']
        self.made = dictionary['kicking']['made']
        self.yards = dictionary['kicking']['yards']
        self.percent = dictionary['kicking']['percent']
        self.xp_attempt = dictionary['kicking']['xp_attempt']
        self.xp_made = dictionary['kicking']['xp_made']
        self.xp_missed = dictionary['kicking']['xp_missed']
        self.xp_blocked = dictionary['kicking']['xp_blocked']
        self.xp_total = dictionary['kicking']['xp_total']

class Defense:

    def __init__(self, dictionary, team_name):
        """team_name passed in to title defense model"""
        # print(dictionary)
        # print('TYPE: ', type(dictionary))
        self.team = team_name
        self.nfl_game_id = dictionary['nfl_game_id']
        self.home_or_away = None
        """must aggregate via method below"""
        self.tackles = 0
        self.assisted_tackles = 0
        self.sacks = 0
        self.interceptions = 0
        self.forced_fumbles = 0
        """retrieve straight from the API per week"""
        self.opponent = dictionary['opponent']
        self.first_downs_allowed = dictionary['totfd']
        self.total_yards_allowed = dictionary['totyds']
        self.passing_yards_allowed = dictionary['pyds']
        self.rushing_yards_allowed = dictionary['ryds']
        self.penalties = dictionary['pen']
        self.penalty_yards = dictionary['penyds']
        self.turnovers = dictionary['trnovr']
        self.total_punts = dictionary['pt']
        self.punt_yards = dictionary['ptyds']
        self.punt_yards_average = dictionary['ptavg']

        game_url = 'https://profootballapi.com/game'
        api_key = 'b3nR2HLfjz41taA7vsi8hqcSJCXmDTOp'
        game_data = {'api_key': api_key, 'game_id': self.nfl_game_id}
        game_response = requests.post(game_url, game_data)
        def_game_dict = json.loads(game_response.text)

        # """determines if home or away team for score purposes"""
        # away = def_game_dict['away']['team']
        # home = def_game_dict['home']['team']
        try:
            if self.team == def_game_dict['away']['team']:
                self.home_or_away = 'away'
            # else:
            #     self.home_or_away = 'home'
        except KeyError:
            self.home_or_away = 'home'

        if self.home_or_away == 'away':
            self.points_allowed = def_game_dict['home_score']
        else:
            self.points_allowed = def_game_dict['away_score']

        """ST stats must aggregate via method"""
        self.xp_attempt = 0
        self.kicking_yards = 0
        self.kicking_attempts = 0
        self.xp_missed = 0
        self.kicks_made = 0
        self.xp_made = 0
        self.xp_blocked = 0
        self.xp_total = 0
        self.kick_returns = 0
        self.kick_returns_long = 0
        self.kick_returns_long_touchdown = 0
        self.kick_returns_touchdowns = 0
        self.punt_returns = 0
        self.punt_returns_long = 0
        self.punt_returns_long_touchdown = 0
        self.punt_returns_touchdowns = 0


    def aggregate_st_data_by_game(self, game_dict):

        try:
            for player_id in game_dict[self.home_or_away]['stats']['kick_return']:
                self.kick_returns += game_dict[self.home_or_away]['stats']['kick_return'][player_id]['returns']
                self.kick_returns_long += game_dict[self.home_or_away]['stats']['kick_return'][player_id]['long']
                self.kick_returns_long_touchdown += game_dict[self.home_or_away]['stats']['kick_return'][player_id]['long_touchdown']
                self.kick_returns_touchdowns += game_dict[self.home_or_away]['stats']['kick_return'][player_id]['touchdowns']

        except KeyError:
            self.kick_returns = 0
            self.kick_returns_long = 0
            self.kick_returns_long_touchdown = 0
            self.kick_returns_touchdowns = 0

        try:
            for player_id in game_dict[self.home_or_away]['stats']['kicking']:
                self.xp_attempt += game_dict[self.home_or_away]['stats']['kicking'][player_id]['xp_attempt']
                self.kicking_yards += game_dict[self.home_or_away]['stats']['kicking'][player_id]['yards']
                self.kicking_attempts += game_dict[self.home_or_away]['stats']['kicking'][player_id]['attempts']
                self.xp_missed += game_dict[self.home_or_away]['stats']['kicking'][player_id]['xp_missed']
                self.kicks_made += game_dict[self.home_or_away]['stats']['kicking'][player_id]['made']
                self.xp_made += game_dict[self.home_or_away]['stats']['kicking'][player_id]['xp_made']
                self.xp_blocked += game_dict[self.home_or_away]['stats']['kicking'][player_id]['xp_blocked']
                self.xp_total += game_dict[self.home_or_away]['stats']['kicking'][player_id]['xp_total']

        except KeyError:
            self.xp_attempt = 0
            self.kicking_yards = 0
            self.kicking_attempts = 0
            self.xp_missed = 0
            self.kicks_made = 0
            self.xp_made = 0
            self.xp_blocked = 0
            self.xp_total = 0

        try:
            for player_id in game_dict[self.home_or_away]['stats']['punt_return']:
                self.punt_returns += game_dict[self.home_or_away]['stats']['punt_return'][player_id]['returns']
                self.punt_returns_long += game_dict[self.home_or_away]['stats']['punt_return'][player_id]['long']
                self.punt_returns_long_touchdown += game_dict[self.home_or_away]['stats']['punt_return'][player_id]['long_touchdown']
                self.punt_returns_touchdowns += game_dict[self.home_or_away]['stats']['punt_return'][player_id]['touchdowns']

        except KeyError:
            self.punt_returns = 0
            self.punt_returns_long = 0
            self.punt_returns_long_touchdown = 0
            self.punt_returns_touchdowns = 0

    def aggregate_def_data_by_player(self, player_response_dictionary):
        def_player_list = []

        for game_id, def_stats in player_response_dictionary.items():
            if game_id != self.nfl_game_id:
                continue

            if isinstance(def_stats, list):
                continue

            for player, player_stats in def_stats.items():
                if isinstance(player_stats, list):
                    continue

                if 'defense' in player_stats:
                    player_stats = player_stats['defense']

                if player_stats['name'] not in def_player_list:
                    def_player_list.append(player_stats['name'])
                    self.tackles += player_stats['tackles']
                    self.assisted_tackles += player_stats['assisted_tackles']
                    self.sacks += player_stats['sacks']
                    self.interceptions += player_stats['interceptions']
                    self.forced_fumbles += player_stats['forced_fumbles']

"""local lookup, if he is not in database, grab him from API."""

"""created and updated field on player model"""
