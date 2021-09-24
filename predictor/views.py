from django.shortcuts import render, redirect
from django.http.response import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from .forms import LeagueRulesForm
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .positions import QB_LIST, RB_LIST, WR_LIST, TE_LIST, K_LIST, DST_LIST, get_position_by_name
from .utilities import api_key, player_url, team_url, get_off_player, get_kicker, get_def_team
from .calculate_average import AveragePlayer, AverageKicker, AverageDefense
from .linear_regression import kicker_fit, predict_kicker, populate_pandas_for_offense, populate_pandas_for_kicker, qb_fit, predict_qb, rb_fit, predict_rb, wr_fit, predict_wr, te_fit, predict_te
# from .multiplyer import calc_QB_score, calc_RB_or_WR_or_TE_score, calc_K_score
from .models import LeagueRulesModel
import pandas as pd
import numpy as np



def index(request):
    return HttpResponseRedirect('/login/')

def home(request):
    context = {}

    set_league_name(request, context)

    average_player = get_average_player(request)

    players = request.session.get('players', [])

    try_delete_player(request, players)

    context['league_list'] = get_league_list(request)

    try_set_player_names(request, context)

    player = try_add_player(request, players, average_player, context)

    set_player_prediction(request, player)

    request.session['players'] = players

    context['players'] = players

    return render(request, 'predictor/home.html', context)

def get_average_player(request):
    player_name = get_chosen_player_name(request)

    if player_name:
        player_position = get_position_by_name(player_name)

        if player_position == 'QB' or player_position == 'RB' or player_position == 'WR' or player_position == 'TE':
            player_list = get_off_player(api_key, player_url, player_name)
            return AveragePlayer(player_list)
        # elif player_position == 'DST':
        #     player_list = get_def_team(api_key, team_url, player_name)
        #     return AverageDefense(player_list)
        elif player_position == 'K':
            player_list = get_kicker(api_key, player_url, player_name)
            return AverageKicker(player_list)


# def get_average_defense(request):
#     defense_name = get_chosen_player_name(request)
#
#     if defense_name:
#         player_position = get_position_by_name(player_name)
#
#         if player_position == 'DST':
#             player_list = get_def_team(api_key, team_url, defense_name)
#             return AverageDefense(player_list)

def set_player_prediction(request, player):
    if not player:
        return

    league = get_league_name(request)

    player_name = player['name']
    player_position = player['position']

    if player_position == 'QB':
        pass_attempts = player['pass_attempts']
        pass_completions = player['pass_completions']
        interceptions = player['interceptions']
        rush_attempts = player['rush_attempts']
        rush_long = player['rush_long']
        rush_long_td = player['rush_long_td']

        if pass_attempts is not None and pass_completions is not None and interceptions is not None and rush_attempts is not None and rush_long is not None and rush_long_td is not None:
            qb_values = qb_predict_control(player_name, float(pass_attempts), float(pass_completions), float(interceptions), float(rush_attempts), float(rush_long), float(rush_long_td))
            player['prediction'] = round(league.calc_QB_score(qb_values),1)
            # player['pass_touchdowns'] = qb_values[0]
            # player['pass_yards'] = qb_values[1]
            # player['rush_touchdowns'] = qb_values[2]
            # player['rush_yards'] = qb_values[3]


    elif player_position == 'RB' or player_position == 'WR' or player_position == 'TE':
        rush_attempts = player['rush_attempts']
        rush_long = player['rush_long']
        rush_long_td = player['rush_long_td']
        receptions = player['receptions']
        receptions_long = player['receptions_long']
        receptions_long_td = player['receptions_long_td']


        if rush_attempts is not None and rush_long is not None and rush_long_td is not None and receptions is not None and receptions_long is not None and receptions_long_td is not None:
            rb_values = rb_predict_control(player_name, float(rush_attempts), float(rush_long), float(rush_long_td), float(receptions), float(receptions_long), float(receptions_long_td))
            player['prediction'] = round(league.calc_RB_or_WR_or_TE_score(rb_values),1)
            # player['rush_touchdowns'] = rb_values[0]
            # player['rush_yards'] = rb_values[1]
            # player['receiving_touchdowns'] = rb_values[2]
            # player['receiving_yards'] = rb_values[3]

    elif player_position == 'K':
        kicking_attempts = player['kicking_attempts']
        kicking_percent = player['kicking_percent']
        xp_attempt = player['xp_attempt']
        xp_missed = player['xp_missed']
        xp_blocked = player['xp_blocked']

        if kicking_attempts is not None and kicking_percent is not None and xp_attempt is not None and xp_missed is not None and xp_blocked is not None:
            k_values = k_predict_control(player_name, float(kicking_attempts), float(kicking_percent), float(xp_attempt), float(xp_missed), float(xp_blocked))
            player['prediction'] = round(league.calc_K_score(k_values),1)
            # player['kicks_made'] = k_values[0]
            # player['kicking_yards'] = k_values[1]
            # player['xp_made'] = k_values[2]


def get_league_name(request):
    if LeagueRulesModel.objects.filter(owner=request.user):
        DEFAULT = LeagueRulesModel.objects.filter(owner=request.user).first()
        return request.GET.get('league_name', DEFAULT)
    else:
        return HttpResponseRedirect('/create/')


def set_league_name(request, context):
    league_name = get_league_name(request)
    print('1: ', league_name)

    context['league_name'] = league_name

    return league_name


# def get_league(request):
#     league_name = get_league_name(request)
#     """hard coded for now, will need to implement a way to select which league object by name. perhaps drop down on predictor page."""
#     print('2', league_name)
#     league = LeagueRulesModel.objects.get(owner=request.user, league_name=league_name)
#     # league = QuerySet
#     print('LEAGUE: ', league.league_name)
#     """not sure if this is desired effect, needs to filter LEAGUERULES objects by user, and filter by selected object"""
#
#     return league


def get_league_list(request):
    """RETURNS ALL LEAGUE OBJECTS TO POPULATE DROP DOWN"""
    return LeagueRulesModel.objects.filter(owner=request.user)


def try_delete_player(request, players):
    delete_player_name = request.GET.get('delete', None)

    if delete_player_name:
        player_index = get_player_index(players, delete_player_name)

        if player_index is not None:
            del players[player_index]


def get_player_index(players, player_name):
    for i in range(len(players)):
        player = players[i]
        if player['name'] == player_name:
            return i
    return None


def get_chosen_player_name(request):
    return request.GET.get('player', None)


def try_set_player_names(request, context):
    player_name = get_chosen_player_name(request)

    if player_name:
        player_position = get_position_by_name(player_name)

        if player_position == 'QB':
            player_names = QB_LIST
        elif player_position == 'RB':
            player_names = RB_LIST
        elif player_position == 'WR':
            player_names = WR_LIST
        elif player_position == 'TE':
            player_names = TE_LIST
        elif player_position == 'K':
            player_names = K_LIST
        # elif player_position == 'DST':
        #     player_names = DST_LIST
        else:
            player_names = QB_LIST
    else:
        player_names = QB_LIST

    context['player_names'] = player_names


def try_add_player(request, players, avg_player, context):
    player_name = get_chosen_player_name(request)
    print(player_name)
    if not player_name:
        return

    player_index = get_player_index(players, player_name)

    if player_index is not None:
        player = players[player_index]
    else:
        player = {}

    player['name'] = player_name
    context['player_name'] = player_name

    player_position = get_position_by_name(player_name)

    player['position'] = player_position
    context['player_position'] = player_position

    if player_position == 'QB':
        player['pass_attempts'] = request.GET.get('pass_attempts', avg_player.avg_passing_attempts)
        player['pass_completions'] = request.GET.get('pass_completions', avg_player.avg_passing_completions)
        player['interceptions'] = request.GET.get('interceptions', avg_player.avg_passing_interceptions)
        player['rush_attempts'] = request.GET.get('rush_attempts', avg_player.avg_rush_attempts)
        player['rush_long'] = request.GET.get('rush_long', avg_player.avg_rush_long)
        player['rush_long_td'] = request.GET.get('rush_long_td', avg_player.avg_rush_long_touchdown)
    elif player_position == 'RB' or player_position == 'WR' or player_position == 'TE':
        player['rush_attempts'] = request.GET.get('rush_attempts', avg_player.avg_rush_attempts)
        player['rush_long'] = request.GET.get('rush_long', avg_player.avg_rush_long)
        player['rush_long_td'] = request.GET.get('rush_long_td', avg_player.avg_rush_long_touchdown)
        player['receptions'] = request.GET.get('receptions', avg_player.avg_receptions)
        player['receptions_long'] = request.GET.get('receptions_long', avg_player.avg_receiving_long)
        player['receptions_long_td'] = request.GET.get('receptions_long_td', avg_player.avg_receiving_long_touchdown)
    elif player_position == 'K':
        player['kicking_attempts'] = request.GET.get('kicking_attempts', avg_player.avg_attempts)
        player['kicking_percent'] = request.GET.get('kicking_percent', avg_player.avg_percent)
        # player['kicking_yards'] = request.GET.get('kicking_yards', '')
        player['xp_attempt'] = request.GET.get('xp_attempts', avg_player.avg_xp_attempt)
        player['xp_missed'] = request.GET.get('xp_missed', avg_player.avg_xp_missed)
        player['xp_blocked'] = request.GET.get('xp_blocked', avg_player.avg_xp_blocked)

    if player_index is not None:
        players[player_index] = player
    else:
        players.append(player)

    return player

def create(request):
    return render(request, 'predictor/league.html')



def log_out(request):
    logout(request)
    return redirect("/")


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # return redirect('/account/profile/{}/'.format(user.id))
            return redirect('/league/')
        else:
            print(form.errors)
    else:
        form = UserCreationForm()
    return render(request, 'predictor/register.html', context={'form': form})


def create_league_form_submit(request):
    if request.method == 'POST':
        form = LeagueRulesForm(request.POST)
        if form.is_valid():
            leaguerulesmodel = form.save(commit=False)
            leaguerulesmodel.owner = request.user
            leaguerulesmodel.save()
            return HttpResponseRedirect('/homepage/')
    else:
        form = LeagueRulesForm()
        return render(request, 'predictor/league.html', {'form': form})


class PlayersView(APIView):
    def get(self, request, *args, **kw):
        position = request.GET.get('position', '').upper()

        players = []

        if position == 'QB':
            players = QB_LIST
        elif position == 'RB':
            players = RB_LIST
        elif position == 'WR':
            players = WR_LIST
        elif position == 'TE':
            players = TE_LIST
        else:
            players = K_LIST

        return Response(players, status=status.HTTP_200_OK)


def qb_predict_control(player_name, pass_attempts, pass_completions, interceptions, rush_attempts, rush_long, rush_long_td):
    # print('step1')
    player_games = get_off_player(api_key, player_url, player_name)
    # print('step2')
    pandas_df = populate_pandas_for_offense(player_games)
    # print('step3')
    pandas_df = pandas_df.dropna(subset=['passing_completions','passing_interceptions', 'passing_touchdowns','passing_yards','rush_attempts', 'rush_long','rush_long_touchdown','rush_touchdowns','rush_yards'])
    # print('step4')
    ptd_fit_model, py_fit_model, rtd_fit_model, ry_fit_model = qb_fit(pandas_df)
    # print('step5')
    predictions = predict_qb(ptd_fit_model, py_fit_model, rtd_fit_model, ry_fit_model, pass_attempts, pass_completions, interceptions, rush_attempts, rush_long, rush_long_td)
    # print('step6')
    return float(predictions[0]), float(predictions[1]), float(predictions[2]), float(predictions[3])


def rb_predict_control(player_name, rush_attempts, rush_long, rush_long_td, receptions, receptions_long, receptions_long_td):
    player_games = get_off_player(api_key, player_url, player_name)
    pandas_df = populate_pandas_for_offense(player_games)
    pandas_df = pandas_df.dropna(subset=['rush_attempts', 'rush_long','rush_long_touchdown','rush_touchdowns','rush_yards', 'receptions', 'receiving_long', 'receiving_long_touchdown', 'receiving_touchdowns', 'receiving_yards'])
    rtd_fit_model, ry_fit_model, rectd_fit_model, recy_fit_model = rb_fit(pandas_df)
    predictions = predict_rb(rtd_fit_model, ry_fit_model, rectd_fit_model, recy_fit_model, rush_attempts, rush_long, rush_long_td, receptions, receptions_long, receptions_long_td)
    return float(predictions[0]), float(predictions[1]), float(predictions[2]), float(predictions[3])


def wr_predict_control(player_name, rush_attempts, rush_long, rush_long_td, receptions, receptions_long, receptions_long_td):
    player_games = get_off_player(api_key, player_url, player_name)
    pandas_df = populate_pandas_for_offense(player_games)
    pandas_df = pandas_df.dropna(subset=['rush_attempts', 'rush_long','rush_long_touchdown','rush_touchdowns','rush_yards', 'receptions', 'receiving_long', 'receiving_long_touchdown', 'receiving_touchdowns', 'receiving_yards'])
    """above is offending line"""
    print(pandas_df)
    rtd_fit_model, ry_fit_model, rectd_fit_model, recy_fit_model = rb_fit(pandas_df)
    print(rtd_fit_model)
    print(ry_fit_model)
    print(rectd_fit_model)
    print(recy_fit_model)
    predictions = predict_rb(rtd_fit_model, ry_fit_model, rectd_fit_model, recy_fit_model, rush_attempts, rush_long, rush_long_td, receptions, receptions_long, receptions_long_td)
    return float(predictions[0]), float(predictions[1]), float(predictions[2]), float(predictions[3])


def te_predict_control(player_name, rush_attempts, rush_long, rush_long_td, receptions, receptions_long, receptions_long_td):
    player_games = get_off_player(api_key, player_url, player_name)
    pandas_df = populate_pandas_for_offense(player_games)
    pandas_df = pandas_df.dropna(subset=['rush_attempts', 'rush_long','rush_long_touchdown','rush_touchdowns','rush_yards', 'receptions', 'receiving_long', 'receiving_long_touchdown', 'receiving_touchdowns', 'receiving_yards'])
    rtd_fit_model, ry_fit_model, rectd_fit_model, recy_fit_model = rb_fit(pandas_df)
    predictions = predict_te(rtd_fit_model, ry_fit_model, rectd_fit_model, recy_fit_model, rush_attempts, rush_long, rush_long_td, receptions, receptions_long, receptions_long_td)
    return float(predictions[0]), float(predictions[1]), float(predictions[2]), float(predictions[3])


def k_predict_control(player_name, kicking_attempts, kicking_percent, xp_attempt, xp_missed, xp_blocked):
    player_games = get_kicker(api_key, player_url, player_name)
    pandas_df = populate_pandas_for_kicker(player_name, player_games)
    # pandas_df = pandas_df.dropna(subset=[''])
    km_l_r_model, ky_l_r_model, xpm_l_r_model = kicker_fit(pandas_df)
    predictions = predict_kicker(km_l_r_model, ky_l_r_model, xpm_l_r_model, kicking_attempts, kicking_percent, xp_attempt, xp_missed, xp_blocked)
    return float(predictions[0]), float(predictions[1]), float(predictions[2])
