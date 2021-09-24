
import pandas as pd
import re
import numpy as np
from .utilities import get_all_kickers, get_all_def, api_key, player_url, team_url


df = pd.read_csv('predictor/positions_csv.csv',usecols=['Rank','Name','Tm','Age','G','GS',
                                            'Cmp','Att','Yds','TD','Int','Att',
                                            'Yds','Y/A','TD','Tgt','Rec','Yds',
                                            'Y/R','TD','FantPos','FantPt','DKPt',
                                            'FDPt','VBD','PosRank','OvRank'])

df = df[pd.notnull(df['FantPos'])]
non_decimal = re.compile(r'[^a-zA_Z]+')
# df = pd.read_csv('_csv.csv',)
# print(df)
WR_LIST = []
RB_LIST = []
QB_LIST = []
TE_LIST = []
K_LIST = []
DST_LIST = ['DAL', 'NYG', 'WAS', 'PHI', 'GB', 'MIN', 'CHI', 'DET', 'CAR', 'NO', 'ATL', 'TB', 'SF', 'STL', 'SEA', 'ARI',
            'NE', 'MIA', 'NYJ', 'BUF', 'PIT', 'CLE', 'CIN', 'BAL', 'IND', 'HOU', 'TEN', 'JAC', 'SD', 'OAK', 'KC', 'DEN']



kicker_list = get_all_kickers(api_key, player_url)
for kicker in kicker_list:
    if kicker.name not in K_LIST:
        K_LIST.append(kicker.name)


# defense_list = get_all_def(api_key, team_url, player_url)
# for defense in defense_list:
#     if defense.team not in DST_LIST:
#         DST_LIST.append(defense.team)
#         print(DST_LIST)

# with open('kicker_csv.csv', 'w') as f:


def parse_name(name):
   fn = name.split()
   first_name = fn[0]
   last_name = ' '.join(fn[1:])
   if "." in first_name:
      first_initial = first_name
   else:
      first_initial = first_name[0]+"."


   return(first_initial+last_name)



def get_players():

    values = {
     'WR': WR_LIST,
     'RB': RB_LIST,
     'QB': QB_LIST,
     'TE': TE_LIST
     }

    for player in df.values:
        position = player[15]
        player_name = player[1].strip('*+')

        values[position].append(parse_name(player_name))


get_players()


def get_position_by_name(player_name):
    position = 'Unknown'
    if player_name in QB_LIST:
        position = 'QB'
    elif player_name in RB_LIST:
        position = 'RB'
    elif player_name in WR_LIST:
        position = 'WR'
    elif player_name in TE_LIST:
        position = 'TE'
    elif player_name in DST_LIST:
        position = 'DST'
    else:
        position = 'K'
    return position
