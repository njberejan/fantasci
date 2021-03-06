# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-12 19:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DefenseModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tackles', models.CharField(default=None, max_length=100, null=True)),
                ('assisted_tackles', models.CharField(default=None, max_length=100, null=True)),
                ('sacks', models.CharField(default=None, max_length=100, null=True)),
                ('interceptions', models.CharField(default=None, max_length=100, null=True)),
                ('forced_fumbles', models.CharField(default=None, max_length=100, null=True)),
                ('xp_attempt', models.CharField(default=None, max_length=100, null=True)),
                ('kicking_yards', models.CharField(default=None, max_length=100, null=True)),
                ('kicking_attempts', models.CharField(default=None, max_length=100, null=True)),
                ('xp_missed', models.CharField(default=None, max_length=100, null=True)),
                ('kicks_made', models.CharField(default=None, max_length=100, null=True)),
                ('xp_made', models.CharField(default=None, max_length=100, null=True)),
                ('xp_blocked', models.CharField(default=None, max_length=100, null=True)),
                ('xp_total', models.CharField(default=None, max_length=100, null=True)),
                ('kick_returns', models.CharField(default=None, max_length=100, null=True)),
                ('kick_returns_long', models.CharField(default=None, max_length=100, null=True)),
                ('kick_returns_long_touchdown', models.CharField(default=None, max_length=100, null=True)),
                ('kick_returns_touchdowns', models.CharField(default=None, max_length=100, null=True)),
                ('punt_returns', models.CharField(default=None, max_length=100, null=True)),
                ('punt_returns_long', models.CharField(default=None, max_length=100, null=True)),
                ('punt_returns_long_touchdown', models.CharField(default=None, max_length=100, null=True)),
                ('punt_returns_touchdowns', models.CharField(default=None, max_length=100, null=True)),
                ('team', models.CharField(max_length=100)),
                ('nfl_game_id', models.CharField(default=None, max_length=100, null=True)),
                ('home_or_away', models.CharField(default=None, max_length=100, null=True)),
                ('points_allowed', models.CharField(default=None, max_length=100, null=True)),
                ('opponent', models.CharField(default=None, max_length=100, null=True)),
                ('first_downs_allowed', models.CharField(default=None, max_length=100, null=True)),
                ('total_yards_allowed', models.CharField(default=None, max_length=100, null=True)),
                ('passing_yards_allowed', models.CharField(default=None, max_length=100, null=True)),
                ('rushing_yards_allowed', models.CharField(default=None, max_length=100, null=True)),
                ('penalties', models.CharField(default=None, max_length=100, null=True)),
                ('penalty_yards', models.CharField(default=None, max_length=100, null=True)),
                ('turnovers', models.CharField(default=None, max_length=100, null=True)),
                ('total_punts', models.CharField(default=None, max_length=100, null=True)),
                ('punt_yards', models.CharField(default=None, max_length=100, null=True)),
                ('punt_yards_average', models.CharField(default=None, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='KickerModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=100, null=True)),
                ('game', models.CharField(default=None, max_length=100, null=True)),
                ('attempts', models.CharField(default=None, max_length=100, null=True)),
                ('made', models.CharField(default=None, max_length=100, null=True)),
                ('yards', models.CharField(default=None, max_length=100, null=True)),
                ('percent', models.CharField(default=None, max_length=100, null=True)),
                ('xp_attempt', models.CharField(default=None, max_length=100, null=True)),
                ('xp_made', models.CharField(default=None, max_length=100, null=True)),
                ('xp_missed', models.CharField(default=None, max_length=100, null=True)),
                ('xp_blocked', models.CharField(default=None, max_length=100, null=True)),
                ('xp_total', models.CharField(default=None, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LeagueRulesModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('league_name', models.CharField(default='My League', max_length=50)),
                ('passing_yards_points', models.FloatField(default=1, null=True)),
                ('passing_yards_number_of_yards', models.FloatField(default=25, null=True)),
                ('passing_touchdowns', models.FloatField(default=6, null=True)),
                ('interceptions', models.FloatField(default=-2, null=True)),
                ('rushing_yards_points', models.FloatField(default=1, null=True)),
                ('rushing_yards_number_of_yards', models.FloatField(default=10, null=True)),
                ('rushing_touchdowns', models.FloatField(default=6, null=True)),
                ('receiving_yards_points', models.FloatField(default=1, null=True)),
                ('receiving_yards_number_of_yards', models.FloatField(default=10, null=True)),
                ('receiving_touchdowns', models.FloatField(default=6, null=True)),
                ('fumble_recovered_for_td', models.FloatField(default=6, null=True)),
                ('two_point_conversions', models.FloatField(default=2, null=True)),
                ('fumbles_lost', models.FloatField(default=-2, null=True)),
                ('XP_made', models.FloatField(default=1, null=True)),
                ('FG_made', models.FloatField(default=3, null=True)),
                ('FG_long_made', models.FloatField(default=5, null=True)),
                ('sacks', models.FloatField(default=1, null=True)),
                ('d_interceptions', models.FloatField(default=2, null=True)),
                ('fumbles_recovered', models.FloatField(default=2, null=True)),
                ('safeties', models.FloatField(default=2, null=True)),
                ('defensive_touchdowns', models.FloatField(default=6, null=True)),
                ('kick_punt_return_tds', models.FloatField(default=6, null=True)),
                ('points_allowed_value1', models.FloatField(default=5, null=True)),
                ('points_allowed_value2', models.FloatField(default=4, null=True)),
                ('points_allowed_value3', models.FloatField(default=3, null=True)),
                ('points_allowed_value4', models.FloatField(default=1, null=True)),
                ('points_allowed_value5', models.FloatField(default=0, null=True)),
                ('points_allowed_value6', models.FloatField(default=-3, null=True)),
                ('points_allowed_value7', models.FloatField(default=-5, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PlayerModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('game', models.CharField(default=None, max_length=100, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('rush_attempts', models.CharField(default=None, max_length=100, null=True)),
                ('rush_yards', models.CharField(default=None, max_length=100, null=True)),
                ('rush_touchdowns', models.CharField(default=None, max_length=100, null=True)),
                ('rush_long', models.CharField(default=None, max_length=100, null=True)),
                ('rush_long_touchdown', models.CharField(default=None, max_length=100, null=True)),
                ('rush_two_point_attempt', models.CharField(default=None, max_length=100, null=True)),
                ('rush_two_point_makes', models.CharField(default=None, max_length=100, null=True)),
                ('receptions', models.CharField(default=None, max_length=100, null=True)),
                ('receiving_yards', models.CharField(default=None, max_length=100, null=True)),
                ('receiving_touchdowns', models.CharField(default=None, max_length=100, null=True)),
                ('receiving_long', models.CharField(default=None, max_length=100, null=True)),
                ('receiving_long_touchdown', models.CharField(default=None, max_length=100, null=True)),
                ('receiving_two_point_attempts', models.CharField(default=None, max_length=100, null=True)),
                ('receiving_two_point_makes', models.CharField(default=None, max_length=100, null=True)),
                ('passing_attempts', models.CharField(default=None, max_length=100, null=True)),
                ('passing_completions', models.CharField(default=None, max_length=100, null=True)),
                ('passing_yards', models.CharField(default=None, max_length=100, null=True)),
                ('passing_touchdowns', models.CharField(default=None, max_length=100, null=True)),
                ('passing_interceptions', models.CharField(default=None, max_length=100, null=True)),
                ('passing_two_point_attempts', models.CharField(default=None, max_length=100, null=True)),
                ('passing_two_point_makes', models.CharField(default=None, max_length=100, null=True)),
                ('total_fumbles', models.CharField(default=None, max_length=100, null=True)),
                ('recovered_fumbles', models.CharField(default=None, max_length=100, null=True)),
                ('team_recovered_fumbles', models.CharField(default=None, max_length=100, null=True)),
                ('fumble_yards', models.CharField(default=None, max_length=100, null=True)),
                ('fumbles_lost', models.CharField(default=None, max_length=100, null=True)),
            ],
        ),
    ]
