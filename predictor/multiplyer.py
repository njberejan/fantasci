# from .linear_regression import *
# from .models import LeagueRulesModel
#
# """if QB"""
# def calc_QB_score(league, values):
#     print('FUNCTION LEAGUE PASSING TD: ', league.passing_touchdowns)
#     pass_td_score = values[0] * league.passing_touchdowns
#     pass_yd_score = values[1] * (league.passing_yards_points/leaguemodel.passing_yards_number_of_yards)
#     rush_td_score = values[2] * league.rushing_touchdowns
#     rush_yd_score = values[3] * (league.rushing_yards_points/league.rushing_yards_number_of_yards)
#     total_score = pass_td_score + pass_yd_score + rush_td_score + rush_yd_score
#     return total_score
#
# """if RB or WR or TE"""
# def calc_RB_or_WR_or_TE_score(league):
#     rush_td_score = rush_td_prediction * league.rushing_touchdowns
#     rush_yd_score = rush_yards_prediction * (league.rushing_yards_points/league.rushing_yards_number_of_yards)
#     rec_td_score = rec_td_prediction * league.receiving_touchdowns
#     rec_yd_score = rec_yards_prediction * (league.rushing_yards_points/league.receiving_yards_number_of_yards)
#     total_score = rush_td_score + rush_yd_score + rec_td_score + rec_yd_score
#     return total_score
#
# """if K"""
# def calc_K_score(league):
#     kicks_made_score = kicks_made_prediction * league.FG_made
#     xp_made_score = xp_made_prediction * league.XP_made
#     #need FG long made?
#     total_score = kicks_made_score + xp_made_score
#     return total_score
