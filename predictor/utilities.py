cd ..import requests
import json

from .objects import Player, Kicker, Defense
from .models import PlayerModel, KickerModel, DefenseModel


api_key = 'b3nR2HLfjz41taA7vsi8hqcSJCXmDTOp'
player_url = 'https://profootballapi.com/players'
team_url = 'https://profootballapi.com/teams'


def get_off_player(api_key, player_url, player_name):

    # data = {'api_key':api_key,'stats_type':'offense','year': '2014', 'player_name': player_name, 'season_type': 'REG'}
    data = {'api_key':api_key,'stats_type':'offense','year': '2014', 'player_name': player_name, 'season_type': 'REG'}

    response = requests.post(player_url, data)
    player_list = []
    the_dict = json.loads(response.text)

    if not isinstance(the_dict, dict):
        print('was not a dictionary...')
        return

    for game, idnumber in the_dict.items():
        for next_layer, dictionary in idnumber.items():
            player = Player(dictionary, game)
            if player.passing_attempts == None and player.rush_attempts == None and player.receptions == None:
                pass
            else:
                player_list.append(player)

    # for player in player_list:
    #     playermodel = PlayerModel(
    #         name=player.name, game=player.game, rush_attempts=player.rush_attempts,
    #         rush_yards=player.rush_yards, rush_touchdowns=player.rush_touchdowns,
    #         rush_long=player.rush_long, rush_long_touchdown=player.rush_long_touchdown,
    #         rush_two_point_attempt=player.rush_two_point_attempt, rush_two_point_makes=player.rush_two_point_makes,
    #         receptions=player.receptions, receiving_yards=player.receiving_yards, receiving_touchdowns=player.receiving_touchdowns,
    #         receiving_long=player.receiving_long, receiving_long_touchdown=player.receiving_long_touchdown,
    #         receiving_two_point_attempts=player.receiving_two_point_attempts, receiving_two_point_makes=player.receiving_two_point_makes,
    #         passing_attempts=player.passing_attempts, passing_completions=player.passing_completions, passing_yards=player.passing_yards,
    #         passing_touchdowns=player.passing_touchdowns, passing_interceptions=player.passing_interceptions,
    #         passing_two_point_attempts=player.passing_two_point_attempts, passing_two_point_makes=player.passing_two_point_makes,
    #         total_fumbles=player.total_fumbles, recovered_fumbles=player.recovered_fumbles,
    #         team_recovered_fumbles=player.team_recovered_fumbles,fumble_yards=player.fumble_yards,
    #         fumbles_lost=player.fumbles_lost,
    #     )
    #     playermodel.save()


    return player_list

def get_kicker(api_key, player_url, player_name):

    data = {'api_key':api_key,'stats_type':'kicking','year': '2014', 'player_name': player_name, 'season_type': 'REG'}
    response = requests.post(player_url, data)
    player_list = []
    the_dict = json.loads(response.text)
    print('THE DICT: ', the_dict)

    for game, idnumber in the_dict.items():
        for player, dictionary in idnumber.items():
            kicker = Kicker(dictionary, game)
            player_list.append(kicker)

    # for kicker in kicker_list:
    #     kickermodel = KickerModel(
    #         name=kicker.name, game=self.game, attempts=kicker.attempts, made=kicker.made, yards=kicker.yards,
    #         percent=kicker.percent, xp_attempt=kicker.xp_attempt, xp_made=kicker.xp_made,
    #         xp_missed=kicker.xp_missed, xp_blocked=kicker.xp_blocked, xp_total=kicker.xp_total,
    #     )
    #     kickermodel.save()

    return player_list


def get_def_team(api_key, team_url, team_name):

    team_data = {'api_key':api_key,'stats_type':'defense','year': '2014', 'team': team_name, 'season_type': 'REG'}
    team_response = requests.post(team_url, team_data)
    game_list = json.loads(team_response.text)
    # print(team_response.text)
    # print('~~~~~~~~~~~~~~~~~~~')
    # print(game_list)
    def_list = []

    """must ping individual player API to get number of tackles, sacks, ints per player per game.
       aggregate_def_data_by_player adds stats for each game, updates model attributes."""

    player_data = {'api_key':api_key,'stats_type':'defense','year': '2014', 'team': team_name, 'season_type': 'REG'}
    player_response = requests.post(player_url, player_data)
    player_response_dictionary = json.loads(player_response.text)
    # print(player_response_dictionary)

    for dictionary in game_list:
        defense = Defense(dictionary, team_name)
        defense.aggregate_def_data_by_player(player_response_dictionary)
        defense.aggregate_st_data_by_game()
        def_list.append(defense)

    # for defense in def_list:
    #     defensemodel = DefenseModel(
    #         tackles=defense.tackles, assisted_tackles=defense.assisted_tackles, sacks=defense.sacks,
    #         interceptions=defense.interceptions, forced_fumbles=defense.forced_fumbles, team=defense.team,
    #         nfl_game_id=defense.nfl_game_id, home_or_away=defense.home_or_away, points_allowed=defense.points_allowed,
    #         opponent=defense.opponent, first_downs_allowed=defense.first_downs_allowed, total_yards_allowed=defense.total_yards_allowed,
    #         passing_yards_allowed=defense.passing_yards_allowed, rushing_yards_allowed=defense.rushing_yards_allowed,
    #         penalties=defense.penalties, penalty_yards=defense.penalty_yards, turnovers=defense.turnovers, total_punts=defense.total_punts,
    #         punt_yards=defense.punt_yards, punt_yards_average=defense.punt_yards_average, xp_attempt=defense.xp_attempt, kicking_yards = defense.kicking_yards,
    #         kicking_attempts=defense.kicking_attempts, xp_missed=defense.xp_missed, kicks_made=defense.kicks_made, xp_made=defense.xp_made, xp_blocked=defense.xp_blocked,
    #         xp_total=defense.xp_total, kick_returns=defense.kick_returns, kick_returns_long=defense.kick_returns_long,
    #         kick_returns_long_touchdown=defense.kick_returns_long_touchdown, kick_returns_touchdowns=defense.kick_returns_touchdowns, punt_returns=defense.punt_returns,
    #         punt_returns_long=defense.punt_returns_long, punt_returns_long_touchdown=defense.punt_returns_long_touchdown, punt_returns_touchdowns=defense.punt_returns_touchdowns,
    #     )
    #     defensemodel.save()

    return def_list


def get_all_off_players(api_key, player_url):

    #data = {'api_key':api_key,'stats_type':'offense','year': '2014', 'player_name': player_name, 'season_type': 'REG'}
    data = {'api_key':api_key,'stats_type':'offense','year': '2014', 'season_type': 'REG'}

    response = requests.post(player_url, data)
    player_list = []
    the_dict = json.loads(response.text)

    for game, idnumber in the_dict.items():
        for next_layer, dictionary in idnumber.items():
            player = Player(dictionary, game)
            if player.name not in player_list:
                player_list.append(player)

    # for player in player_list:
    #     playermodel = PlayerModel(
    #         name=player.name, game=player.game, rush_attempts=player.rush_attempts,
    #         rush_yards=player.rush_yards, rush_touchdowns=player.rush_touchdowns,
    #         rush_long=player.rush_long, rush_long_touchdown=player.rush_long_touchdown,
    #         rush_two_point_attempt=player.rush_two_point_attempt, rush_two_point_makes=player.rush_two_point_makes,
    #         receptions=player.receptions, receiving_yards=player.receiving_yards, receiving_touchdowns=player.receiving_touchdowns,
    #         receiving_long=player.receiving_long, receiving_long_touchdown=player.receiving_long_touchdown,
    #         receiving_two_point_attempts=player.receiving_two_point_attempts, receiving_two_point_makes=player.receiving_two_point_makes,
    #         passing_attempts=player.passing_attempts, passing_completions=player.passing_completions, passing_yards=player.passing_yards,
    #         passing_touchdowns=player.passing_touchdowns, passing_interceptions=player.passing_interceptions,
    #         passing_two_point_attempts=player.passing_two_point_attempts, passing_two_point_makes=player.passing_two_point_makes,
    #         total_fumbles=player.total_fumbles, recovered_fumbles=player.recovered_fumbles,
    #         team_recovered_fumbles=player.team_recovered_fumbles,fumble_yards=player.fumble_yards,
    #         fumbles_lost=player.fumbles_lost,
    #     )
    #     playermodel.save()

    return player_list

def get_all_kickers(api_key, player_url):

    data = {'api_key':api_key,'stats_type':'kicking','year': '2014', 'season_type': 'REG'}
    response = requests.post(player_url, data)
    kicker_list = []
    the_dict = json.loads(response.text)


    for game, idnumber in the_dict.items():
        for next_layer, dictionary in idnumber.items():
            kicker = Kicker(dictionary, game)
            kicker_list.append(kicker)

    # for kicker in kicker_list:
    #     kickermodel = KickerModel(
    #         name=kicker.name, game=kicker.game, attempts=kicker.attempts, made=kicker.made, yards=kicker.yards,
    #         percent=kicker.percent, xp_attempt=kicker.xp_attempt, xp_made=kicker.xp_made,
    #         xp_missed=kicker.xp_missed, xp_blocked=kicker.xp_blocked, xp_total=kicker.xp_total,
    #     )
    #     kickermodel.save()

    return kicker_list


def get_all_def(api_key, team_url, player_url):
    # team_list = ['DAL', 'NYG', 'WAS', 'PHI', 'GB', 'MIN', 'CHI', 'DET', 'CAR', 'NO', 'ATL', 'TB', 'SF', 'STL', 'SEA', 'ARI',
    #             'NE', 'MIA', 'NYJ', 'BUF', 'PIT', 'CLE', 'CIN', 'BAL', 'IND', 'HOU', 'TEN', 'JAC', 'SD', 'OAK', 'KC', 'DEN']

    # for team_name in team_list:

    team_dict = {'DAL': 'DAL', 'NYG': 'NYG', 'WAS': 'WAS', 'PHI': 'PHI', 'GB': 'GB', 'MIN': 'MIN', 'CHI': 'CHI', 'DET': 'DET', 'CAR': 'CAR',
                'NO': 'NO', 'ATL': 'ATL', 'TB': 'TB', 'SF': 'SF', 'STL': 'STL', 'SEA': 'SEA', 'ARI': 'ARI', 'NE': 'NE', 'MIA': 'MIA', 'NYJ': 'NYJ',
                'BUF': 'BUF', 'PIT': 'PIT', 'CLE': 'CLE', 'CIN': 'CIN', 'BAL': 'BAL', 'IND': 'IND', 'HOU': 'HOU', 'TEN': 'TEN', 'JAX': 'JAX',
                'SD': 'SD', 'OAK': 'OAK', 'KC': 'KC', 'DEN': 'DEN'}

    def_list = []

    for team_name, value in team_dict.items():

        team_data = {'api_key':api_key,'stats_type':'defense','year': '2014', 'team': value, 'season_type': 'REG'}
        team_response = requests.post(team_url, team_data)
        game_list = json.loads(team_response.text)

        player_data = {'api_key':api_key,'stats_type':'defense','year': '2014', 'team': team_name, 'season_type': 'REG'}
        player_response = requests.post(player_url, player_data)
        player_response_dictionary = json.loads(player_response.text)
        # print(player_response_dictionary)

        for dictionary in game_list:
            defense = Defense(dictionary, team_name)
            game_url = 'https://profootballapi.com/game'
            api_key = 'b3nR2HLfjz41taA7vsi8hqcSJCXmDTOp'
            game_data = {'api_key': api_key, 'game_id': defense.nfl_game_id}
            game_response = requests.post(game_url, game_data)
            game_dict = json.loads(game_response.text)


            defense.aggregate_def_data_by_player(player_response_dictionary)
            defense.aggregate_st_data_by_game(game_dict)
            def_list.append(defense)

    # for defense in def_list:
    #     defensemodel = DefenseModel(
    #         tackles=defense.tackles, assisted_tackles=defense.assisted_tackles, sacks=defense.sacks,
    #         interceptions=defense.interceptions, forced_fumbles=defense.forced_fumbles, team=defense.team,
    #         nfl_game_id=defense.nfl_game_id, home_or_away=defense.home_or_away, points_allowed=defense.points_allowed,
    #         opponent=defense.opponent, first_downs_allowed=defense.first_downs_allowed,
    #         total_yards_allowed=defense.total_yards_allowed,
    #         passing_yards_allowed=defense.passing_yards_allowed, rushing_yards_allowed=defense.rushing_yards_allowed,
    #         penalties=defense.penalties, penalty_yards=defense.penalty_yards, turnovers=defense.turnovers,
    #         total_punts=defense.total_punts,
    #         punt_yards=defense.punt_yards, punt_yards_average=defense.punt_yards_average, xp_attempt=defense.xp_attempt,
    #         kicking_yards=defense.kicking_yards,
    #         kicking_attempts=defense.kicking_attempts, xp_missed=defense.xp_missed, kicks_made=defense.kicks_made,
    #         xp_made=defense.xp_made, xp_blocked=defense.xp_blocked,
    #         xp_total=defense.xp_total, kick_returns=defense.kick_returns, kick_returns_long=defense.kick_returns_long,
    #         kick_returns_long_touchdown=defense.kick_returns_long_touchdown,
    #         kick_returns_touchdowns=defense.kick_returns_touchdowns, punt_returns=defense.punt_returns,
    #         punt_returns_long=defense.punt_returns_long,
    #         punt_returns_long_touchdown=defense.punt_returns_long_touchdown,
    #         punt_returns_touchdowns=defense.punt_returns_touchdowns,
    #     )
    #     defensemodel.save()

    return def_list
