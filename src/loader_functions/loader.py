import pandas as pd
import time
import numpy as np

from src.loader_functions.get_matcher_per_player import get_matcher_per_player
from src.loader_functions.get_player_race import get_player_race

from src.config import PATH_TO_PLAYERS

def _load_players() -> pd.DataFrame:
    df = pd.read_csv(PATH_TO_PLAYERS, sep = ';')
    return df
# end def

def load_data(idx : int):
    time.sleep(np.random.uniform(30, 80))
    while True:
        df_players = _load_players()
        df_players_filtered = df_players[df_players['is_loaded'] != 1].reset_index(drop = True)

        if df_players_filtered.empty:
            print("All players are loaded. Exit.")
            break
        # end if

        cur_player = df_players_filtered.iloc[idx]['player']
        print(f'Total players : {len(df_players)} | left {len(df_players_filtered)} | Now: {cur_player} | PRC : {1 - (len(df_players_filtered) / len(df_players)):.4f}')

        time.sleep(np.random.uniform(10, 60))
        df_curr = get_matcher_per_player(cur_player)
        race = get_player_race(cur_player)

        csv_path = f'./data/{cur_player}.csv'
        df_curr.to_csv(csv_path, index = False, sep = ';')

        df_players = _load_players()
        existing_players = set(df_players['player'])

        found_players = set(df_curr['player'])
        new_players = found_players - existing_players

        mask = df_players['player'] == cur_player
        df_players.loc[mask, 'is_loaded'] = 1
        df_players.loc[mask, 'path'] = csv_path
        df_players.loc[mask, 'race'] = race

        if new_players:
            df_new = pd.DataFrame({
                'player': list(new_players),
                'is_loaded': 0,
                'path': None,
                'race': None
            })
            df_players = pd.concat([df_players, df_new], ignore_index=True)
        # end if

        df_players.to_csv(PATH_TO_PLAYERS, sep = ';', index = False)
    # end while
# end def
