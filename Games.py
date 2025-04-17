import pathlib
import sys
import pandas as pd
import numpy as np

PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))
MAIN_DIR: pathlib.Path = PROJECT_ROOT.joinpath("2022_NFL_ANALYTICS")
DATA_DIR: pathlib.Path = MAIN_DIR.joinpath("Data")
NEW_DATA_DIR: pathlib.Path =MAIN_DIR.joinpath("Cleaned_Data")
games_data: pathlib.Path = DATA_DIR.joinpath("games.csv")

df = pd.read_csv(games_data)

df_new = df[['week', 'homeTeamAbbr', 'homeFinalScore', 'visitorTeamAbbr', 'visitorFinalScore']]
df_new['Home_winner'] = np.where(df_new['homeFinalScore']>df_new['visitorFinalScore'], 'Y', 'N')
df_new['tie']=np.where(df_new['homeFinalScore']==df_new['visitorFinalScore'],'T','')

df_new['Winner'] = np.where(df_new['Home_winner']=='Y',df_new['homeTeamAbbr'], df_new['visitorTeamAbbr'])
df_new['Loser'] = np.where(df_new['Home_winner']=='N',df_new['homeTeamAbbr'], df_new['visitorTeamAbbr'])

 
file_path: pathlib.Path = NEW_DATA_DIR.joinpath("games_new.csv")
df_new.to_csv(file_path, index=False)

print(df_new[0:60])