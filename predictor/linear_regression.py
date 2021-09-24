import pandas as pd
import numpy as np
from collections import defaultdict
from .utilities import get_off_player
from sklearn.linear_model import LinearRegression
from .objects import *

api_key = 'b3nR2HLfjz41taA7vsi8hqcSJCXmDTOp'
player_url = 'https://profootballapi.com/players'
# player_name = 'C.Newton'

# the_response_dict = get_off_player(api_key, player_url, player_name)


# player_game_stats = []
# for game in the_response_dict:
#     player = Player(value)
#     player_game_stats.append(player)

def populate_pandas_for_offense(the_response_dict):

    offense_dict = defaultdict(list)
    for player in the_response_dict:
        for key, value in player.__dict__.items():
            offense_dict[key].append(value)

    return offense_dict

# def populate_pandas_for_offense(the_response_dict):
 """ old method, see above for refactor 9/15/16 """
#     name=[]
#     rush_attempts = []
#     rush_yards =[]
#     rush_touchdowns = []
#     rush_long = []
#     rush_long_touchdown = []
#     rush_two_point_attempt = []
#     rush_two_point_makes = []
#
#     receptions = []
#     receiving_yards = []
#     receiving_touchdowns = []
#     receiving_long = []
#     receiving_long_touchdown = []
#     receiving_two_point_attempts = []
#     receiving_two_point_makes = []
#
#     passing_attempts = []
#     passing_completions = []
#     passing_yards = []
#     passing_touchdowns = []
#     passing_interceptions = []
#     passing_two_point_attempts = []
#     passing_two_point_makes = []
#
#     total_fumbles = []
#     recovered_fumbles = []
#     team_recovered_fumbles = []
#     fumble_yards = []
#     fumbles_lost = []
#
#     for player_game in the_response_dict:
#         name.append(player_game.name)
#         rush_attempts.append(player_game.rush_attempts)
#         rush_yards.append(player_game.rush_yards)
#         rush_touchdowns.append(player_game.rush_touchdowns)
#         rush_long.append(player_game.rush_long)
#         rush_long_touchdown.append(player_game.rush_long_touchdown)
#         rush_two_point_attempt.append(player_game.rush_two_point_attempt)
#         rush_two_point_makes.append(player_game.rush_two_point_makes)
#
#         receptions.append(player_game.receptions)
#         receiving_yards.append(player_game.receiving_yards)
#         receiving_touchdowns.append(player_game.receiving_touchdowns)
#         receiving_long.append(player_game.receiving_long)
#         receiving_long_touchdown.append(player_game.receiving_long_touchdown)
#         receiving_two_point_attempts.append(player_game.receiving_two_point_attempts)
#         receiving_two_point_makes.append(player_game.receiving_two_point_makes)
#
#         passing_attempts.append(player_game.passing_attempts)
#         passing_completions.append(player_game.passing_completions)
#         passing_yards.append(player_game.passing_yards)
#         passing_touchdowns.append(player_game.passing_touchdowns)
#         passing_interceptions.append(player_game.passing_interceptions)
#         passing_two_point_attempts.append(player_game.passing_two_point_attempts)
#         passing_two_point_makes.append(player_game.passing_two_point_makes)
#
#         total_fumbles.append(player_game.total_fumbles)
#         recovered_fumbles.append(player_game.recovered_fumbles)
#         team_recovered_fumbles.append(player_game.team_recovered_fumbles)
#         fumble_yards.append(player_game.fumble_yards)
#         fumbles_lost.append(player_game.fumbles_lost)
#
#     data = {'Name': name,
#         'rush_attempts': rush_attempts,
#         'rush_yards': rush_yards,
#         'rush_touchdowns': rush_touchdowns,
#         'rush_long': rush_long,
#         'rush_long_touchdown': rush_long_touchdown,
#         'rush_two_point_attempt': rush_two_point_attempt,
#         'rush_two_point_makes': rush_two_point_makes,
#         'receptions': receptions,
#         'receiving_yards': receiving_yards,
#         'receiving_touchdowns': receiving_touchdowns,
#         'receiving_long': receiving_long,
#         'receiving_long_touchdown': receiving_long_touchdown,
#         'receiving_two_point_attempts': receiving_two_point_attempts,
#         'receiving_two_point_makes': receiving_two_point_makes,
#         'passing_attempts': passing_attempts,
#         'passing_completions': passing_completions,
#         'passing_yards': passing_yards,
#         'passing_touchdowns': passing_touchdowns,
#         'passing_interceptions': passing_interceptions,
#         'passing_two_point_attempts': passing_two_point_attempts,
#         'passing_two_point_makes': passing_two_point_makes,
#         'total_fumbles': total_fumbles,
#         'recovered_fumbles': recovered_fumbles,
#         'team_recovered_fumbles': team_recovered_fumbles,
#         'fumble_yards': fumble_yards,
#         'fumbles_lost': fumbles_lost}
#     # print(data)
#
#     df = pd.DataFrame(data)
#     return df

def populate_pandas_for_kicker(player_name, the_response_dict):

        kicker_dict = defaultdict(list)
        for player in the_response_dict:
            for key, value in player.__dict__.items():
                offense_dict[key].append(value)

        return kicker_dict


# def populate_pandas_for_kicker(player_name, the_response_dict):
     """ old method, see above for refactor 9/15/16 """
    # attempts = []
    # made = []
    # yards = []
    # percent = []
    # xp_attempts = []
    # xp_made = []
    # xp_missed = []
    # xp_blocked = []
    # xp_total = []
    #
    # for player_game in the_response_dict:
    #     attempts.append(player_game.attempts)
    #     made.append(player_game.made)
    #     yards.append(player_game.yards)
    #     percent.append(player_game.percent)
    #     xp_attempts.append(player_game.xp_attempt)
    #     xp_made.append(player_game.xp_made)
    #     xp_missed.append(player_game.xp_missed)
    #     xp_blocked.append(player_game.xp_blocked)
    #     xp_total.append(player_game.xp_total)
    #
    # data = {'kicking_attempts': attempts,
    #         'kicks_made': made,
    #         'kicking_yards': yards,
    #         'kicking_percent': percent,
    #         'xp_attempts': xp_attempts,
    #         'xp_made': xp_made,
    #         'xp_missed': xp_missed,
    #         'xp_blocked': xp_blocked,
    #         'xp_total': xp_total}
    #
    # df = pd.DataFrame(data)
    #
    # return df


def qb_fit(df):
    X = df[['passing_attempts',
            'passing_completions',
            'passing_interceptions']]

    y = df['passing_touchdowns']

    X2 = df[['passing_attempts',
             'passing_completions',
             'passing_interceptions']]

    y2 = df['passing_yards']

    X3 = df[['rush_attempts',
             'rush_long',
             'rush_long_touchdown']]

    y3 = df['rush_touchdowns']

    X4 = df[['rush_attempts',
             'rush_long',
             'rush_long_touchdown']]

    y4 = df['rush_yards']
    ##Still need to make the LR model for the other scoring variables

    ptd_l_r_model = LinearRegression()
    py_l_r_model = LinearRegression()
    rtd_l_r_model = LinearRegression()
    ry_l_r_model = LinearRegression()

    ptd_fit_model = ptd_l_r_model.fit(X, y)
    py_fit_model = py_l_r_model.fit(X2, y2)
    rtd_fit_model = rtd_l_r_model.fit(X3, y3)
    ry_fit_model = ry_l_r_model.fit(X4, y4)

    return ptd_fit_model, py_fit_model, rtd_fit_model, ry_fit_model


def rb_fit(df):
    X = df[['rush_attempts',
            'rush_long',
            'rush_long_touchdown']]

    y = df['rush_touchdowns']

    X2 = df[['rush_attempts',
             'rush_long',
             'rush_long_touchdown']]

    y2 = df['rush_yards']

    X3 = df[['receptions',
             'receiving_long',
             'receiving_long_touchdown']]

    y3 = df['receiving_touchdowns']

    X4 = df[['receptions',
             'receiving_long',
             'receiving_long_touchdown']]

    y4 = df['receiving_yards']

    rtd_l_r_model = LinearRegression()
    ry_l_r_model = LinearRegression()
    rectd_l_r_model = LinearRegression()
    recy_l_r_model = LinearRegression()

    rtd_fit_model = rtd_l_r_model.fit(X,y)
    ry_fit_model = ry_l_r_model.fit(X2, y2)
    rectd_fit_model = rectd_l_r_model.fit(X3, y3)
    recy_fit_model = recy_l_r_model.fit(X4, y4)

    return rtd_fit_model, ry_fit_model, rectd_fit_model, recy_fit_model

##Put RB predict here

def wr_fit(df):

    X = df[['receptions',
             'receiving_long',
             'receiving_long_touchdown']]

    y = df['receiving_touchdowns']

    X2 = df[['receptions',
             'receiving_long',
             'receiving_long_touchdown']]

    y2 = df['receiving_yards']

    rectd_l_r_model = LinearRegression()
    ry_l_r_model = LinearRegression()

    rectd_fit_model = rectd_l_r_model.fit(X,y)
    ry_fit_model = ry_l_r_model.fit(X2, y2)

    return rectd_fit_model, ry_fit_model

def te_fit(df):

    X = df[['receptions',
             'receiving_long',
             'receiving_long_touchdown']]

    y = df['receiving_touchdowns']

    X2 = df[['receptions',
             'receiving_long',
             'receiving_long_touchdown']]

    y2 = df['receiving_yards']

    rectd_l_r_model = LinearRegression()
    ry_l_r_model = LinearRegression()

    rectd_fit_model = rectd_l_r_model.fit(X,y)
    ry_fit_model = ry_l_r_model.fit(X2, y2)

    return rectd_fit_model, ry_fit_model

def kicker_fit(df):
    X = df[['kicking_attempts',
            'kicking_percent']]

    y = df['kicks_made']

    X2 = df[['kicking_attempts',
             'kicking_percent']]

    y2 = df['kicking_yards']

    X3 = df[['xp_attempts',
            'xp_missed',
            'xp_blocked']]

    y3 = df['xp_made']

    km_l_r_model = LinearRegression()
    ky_l_r_model = LinearRegression()
    xpm_l_r_model = LinearRegression()

    km_fit_model = km_l_r_model.fit(X,y)
    ky_fit_model = ky_l_r_model.fit(X2,y2)
    xpm_fit_model = xpm_l_r_model.fit(X3,y3)

    return km_fit_model, ky_fit_model, xpm_fit_model




def predict_qb(ptd_fit_model, py_fit_model, rtd_fit_model, ry_fit_model, a,b,c,d,e,f):

    pass_td_prediction = ptd_fit_model.predict([[a,b,c,]])
    pass_yards_prediction = py_fit_model.predict([[a,b,c]])
    rush_td_prediction = rtd_fit_model.predict([[d,e,f]])
    rush_yards_prediction = ry_fit_model.predict([[d,e,f]])

    return pass_td_prediction, pass_yards_prediction, rush_td_prediction, rush_yards_prediction

def predict_rb(rtd_fit_model, ry_fit_model, rectd_fit_model, recy_fit_model,a,b,c,d,e,f):

    rush_td_prediction = rtd_fit_model.predict([[a,b,c]])
    rush_yards_prediction = ry_fit_model.predict([[a,b,c]])
    rec_td_prediction = rectd_fit_model.predict([[d,e,f]])
    rec_yards_prediction = recy_fit_model.predict([[d,e,f]])

    return rush_td_prediction, rush_yards_prediction, rec_td_prediction, rec_yards_prediction

def predict_wr(rtd_fit_model, ry_fit_model, rectd_fit_model, recy_fit_model,a,b,c,d,e,f):

    rush_td_prediction = rtd_fit_model.predict([[a,b,c]])
    rush_yards_prediction = ry_fit_model.predict([[a,b,c]])
    rec_td_prediction = rectd_fit_model.predict([[d,e,f]])
    rec_yards_prediction = recy_fit_model.predict([[d,e,f]])

    return rush_td_prediction, rush_yards_prediction, rec_td_prediction, rec_yards_prediction

def predict_te(rtd_fit_model, ry_fit_model, rectd_fit_model, recy_fit_model,a,b,c,d,e,f):

    rush_td_prediction = rtd_fit_model.predict([[a,b,c]])
    rush_yards_prediction = ry_fit_model.predict([[a,b,c]])
    rec_td_prediction = rectd_fit_model.predict([[d,e,f]])
    rec_yards_prediction = recy_fit_model.predict([[d,e,f]])

    return rush_td_prediction, rush_yards_prediction, rec_td_prediction, rec_yards_prediction

def predict_kicker(km_fit_model, ky_fit_model, xpm_fit_model,a,b,c,d,e):
    kicks_made_prediction = km_fit_model.predict([[a,b]])
    kick_yards_prediction = ky_fit_model.predict([[a,b]])
    xp_made_prediction = xpm_fit_model.predict([[c,d,e]])

    return kicks_made_prediction, kick_yards_prediction, xp_made_prediction







# def predict_kicker(player_name):
#     name = []
#     attempts = []
#     made = []
#     yards = []
#     percent = []
#     xp_attempt = []
#     xp_made = []
#     xp_missed = []
#     xp_blocked = []
#     xp_total = []
#
#     for player_game in the_response_dict:
#         name.append(player_game.name)
#         attempts.append(player_game.attempts)
#         made.append(player_game.made)
#         yards.append(player_game.yards)
#         percent.append(player_game.percent)
#         xp_attempt.append(player_game.xp_attempt)
#         xp_made.append(player_game.xp_made)
#         xp_missed.append(player_game.xp_missed)
#         xp_blocked.append(player_game.xp_blocked)
#         xp_total.append(player_game.xp_total)
#
#         data = {'name':name,
#                 'attempts':attempts,
#                 'made': made,
#                 'yards': yards,
#                 'percent': percent,
#                 'xp_attempt': xp_attempt,
#                 'xp_made': xp_made,
#                 'xp_missed': xp_missed,
#                 'xp_blocked': xp_blocked,
#                 'xp_total': xp_total}
#
#         df = pd.DataFrame(data)
#
# def predict_special_teams(team):
#
#     returns = []
#     average = []
#     touchdowns = []
#     long_ = []
#     long_touchdown = []
#     punt_returns = []
#
#     for player_game in the_response_dict:
#         returns.append(player_game.returns)
#         average.append(player_game.average)
#         touchdowns.append(player_game.touchdowns)
#         long_.append(player_game.long)
#         long_touchdown.append(player_game.long_touchdown)
#         punt_returns.append(player_game.punt_returns
#
#     data = {'returns': returns,
#             'average': average,
#             'touchdowns': touchdowns,
#             'long': long,
#             'long_touchdown': long_touchdown,
#             'punt_returns': punt_returns}
#
#     df = pd.DataFrame(data)
#
# def predict_defense(team):
#     tackles = []
#     assisted_tackles = []
#     sacks = []
#     interceptions = []
#     forced_fumbles = []
#     # opponent = []
#     first_downs_allowed = []
#     total_yards_allowed = []
#     passing_yards_allowed = []
#     rushing_yards_allowed = []
#     penalties = []
#     penalty_yards = []
#     turnovers = []
#     total_punts = []
#     punt_yards = []
#     punt_yards_average = []
#
#     for team_game in the_response_dict:
#         tackles.append(team_game.tackles)
#         assisted_tackles.append(team_game.assisted_tackles)
#         sacks.append(team_game.sacks)
#         interceptions.append(team_game.interceptions)
#         forced_fumbles.append(team_game.forced_fumbles)
#         #opponent.append(team_game.opponent)
#         first_downs_allowed.append(team_game.first_downs_allowed)
#         total_yards_allowed.append(team_game.total_yards_allowed)
#         passing_yards_allowed.append(team_game.passing_yards_allowed)
#         rushing_yards_allowed.append(team_game.rushing_yards_allowed)
#         penalties.append(team_game.penalties)
#         penalty_yards.append(team_game.penalty_yards)
#         turnovers.append(team_game.turnovers)
#         total_punts.append(team_game.total_punts)
#         punt_yards.append(team_game.punt_yards)
#         punt_yards_average.append(team_game.punt_yards_average)
#
#         data = {'tackles': tackles,
#                 'assisted_tackles': assisted_tackles,
#                 'sacks': sacks,
#                 'interceptions': interceptions,
#                 'forced_fumbles': forced_fumbles,
#                 #'opponent': opponent,
#                 'first_downs_allowed': first_downs_allowed,
#                 'total_yards_allowed': total_yards_allowed,
#                 'passing_yards_allowed': passing_yards_allowed,
#                 'rushing_yards_allowed': rushing_yards_allowed,
#                 'penalties': penalties,
#                 'penalty_yards': penalty_yards,
#                 'turnovers': turnovers,
#                 'total_punts': total_punts,
#                 'punt_yards': punt_yards,
#                 'punt_yards_average': punt_yards_average}
#
#         df = pd.DataFrame(data)
