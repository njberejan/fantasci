"""GET request in views, functions to instantiate models called in views"""

import requests

#player_name = Player.name
#kicker_name = Kicker.name
#def_team = Defense.name
#spec_team = SpecTeam.name

player_name = input('enter player name: ')
year = input('enter a year: ')

url = 'https://profootballapi.com/players'
api_key = 'b3nR2HLfjz41taA7vsi8hqcSJCXmDTOp'

off_player = {'api_key': api_key,'stats_type':'offense','year': year, 'season_type': 'REG', 'player_name': player_name}
kicker = {'api_key': api_key,'stats_type':'kicking','year': year, 'season_type': 'REG', 'player_name': kicker_name}
defense = {'api_key': api_key,'stats_type':'defense','year': year, 'season_type': 'REG', 'team': def_team}
spec_teams = {'api_key': api_key,'stats_type':'special_teams','year': year, 'season_type': 'REG', 'team': spec_team}

off_response = requests.post(url, off_player)
kick_response = requests.post(url, kicker)
def_response = requests.post(url, defense)
spec_teams_requests.post(url, spec_teams)
