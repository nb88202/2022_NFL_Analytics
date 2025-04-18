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
players_data: pathlib.Path = DATA_DIR.joinpath("players.csv")

df = pd.read_csv(players_data)

df_new = df[['nflId','position','displayName']]

 
file_path: pathlib.Path = NEW_DATA_DIR.joinpath("players_new.csv")
df_new.to_csv(file_path, index=False)

print(df_new[0:60])