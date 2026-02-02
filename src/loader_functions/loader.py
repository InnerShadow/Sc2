from tqdm import tqdm
import os
import time

import pandas as pd
import numpy as np

from src.loader_functions.get_liquipedia_tournaments import get_liquipedia_tournaments
from src.loader_functions.get_liquipedia_tornament_info import get_liquipedia_tornament_info
from src.loader_functions.get_aligulac_matches import get_aligulac_matches
from src.loader_functions.json_functions import load_processed_tournaments, save_processed_tournaments

from src.config import LIQUIPEDIA_URLS, SAVE_PATH, SAVE_PATH_TOURNAMENTS, LIQUIPEDIA_URLS_ACTUAL

def load_data():

    if os.path.exists(SAVE_PATH):
        df = pd.read_csv(SAVE_PATH, sep = ';')
    else:
        df = pd.DataFrame(
            columns = [
                'date',
                'player',
                'player_race',
                'player_score',
                'player_id',
                'opponent',
                'opponent_race',
                'opponent_score',
                'opponent_id',
                'score_match',
                'tier',
                'url'
            ]
            )
    # end if

    processed_tournaments = load_processed_tournaments(SAVE_PATH_TOURNAMENTS)

    for url, tier in LIQUIPEDIA_URLS.items():
        print(f'start : {url}')
        tournaments = get_liquipedia_tournaments(url)
        time.sleep(30 + np.random.uniform(10, 30))
        for tournament in tqdm(tournaments):
            if tournament in processed_tournaments:
                continue
            # end if
            aligulac_url = get_liquipedia_tornament_info(tournament)
            time.sleep(30 + np.random.uniform(10, 30))
            if aligulac_url is not None and aligulac_url not in df['url'].unique():
                aligulac_data = get_aligulac_matches(aligulac_url)

                aligulac_data['tier'] = tier
                aligulac_data['url'] = aligulac_url
                aligulac_data['tournament'] = tournament

                df = pd.concat([df, aligulac_data]).reset_index(drop = True)
                df.to_csv(SAVE_PATH, sep = ';', index = False)
            # end if
            processed_tournaments.add(tournament)
            save_processed_tournaments(SAVE_PATH_TOURNAMENTS, processed_tournaments)
        # end for
    # end for
# end def

def load_data_actual():
    if os.path.exists(SAVE_PATH):
        df = pd.read_csv(SAVE_PATH, sep=';')
    else:
        df = pd.DataFrame(
            columns=[
                'date',
                'player',
                'player_race',
                'player_score',
                'player_id',
                'opponent',
                'opponent_race',
                'opponent_score',
                'opponent_id',
                'score_match',
                'tier',
                'url',
                'tournament'
            ]
        )
    # end if 

    processed_tournaments = load_processed_tournaments(SAVE_PATH_TOURNAMENTS)

    for url, tier in LIQUIPEDIA_URLS_ACTUAL.items():
        print(f'start : {url}')
        tournaments = get_liquipedia_tournaments(url)
        time.sleep(30 + np.random.uniform(10, 30))

        for tournament in tqdm(tournaments):

            if 'tournament' in df.columns:
                if (df['tournament'] == tournament).any():
                    processed_tournaments.add(tournament)
                    continue
                # end if
            # end if

            aligulac_url = get_liquipedia_tornament_info(tournament)
            time.sleep(30 + np.random.uniform(10, 30))

            if aligulac_url is None:
                continue
            # end if

            if aligulac_url in df['url'].unique():
                processed_tournaments.add(tournament)
                continue
            # end if

            aligulac_data = get_aligulac_matches(aligulac_url)

            if aligulac_data is None or aligulac_data.empty:
                continue
            # end if

            aligulac_data['tier'] = tier
            aligulac_data['url'] = aligulac_url
            aligulac_data['tournament'] = tournament

            df = pd.concat([df, aligulac_data], ignore_index=True)
            df.to_csv(SAVE_PATH, sep=';', index=False)

            processed_tournaments.add(tournament)
            save_processed_tournaments(SAVE_PATH_TOURNAMENTS, processed_tournaments)
    # end for
# end def
