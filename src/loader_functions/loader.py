from tqdm import tqdm
import os
import time

import pandas as pd
import numpy as np

from src.loader_functions.get_liquipedia_tournaments import get_liquipedia_tournaments
from src.loader_functions.get_liquipedia_tornament_info import get_liquipedia_tornament_info
from src.loader_functions.get_aligulac_matches import get_aligulac_matches
from src.loader_functions.json_functions import load_processed_tournaments, save_processed_tournaments

from src.config import LIQUIPEDIA_URLS, SAVE_PATH, SAVE_PATH_TOURNAMENTS

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
        time.sleep(60 + np.random.uniform(10, 30))
        for tournament in tqdm(tournaments):
            if tournament not in df['url'].tolist():
                if tournament in processed_tournaments:
                    continue
                # end if
                aligulac_url = get_liquipedia_tornament_info(tournament)
                # print(f'{aligulac_url} FROM {tournament}')
                time.sleep(60 + np.random.uniform(10, 30))
                if aligulac_url is not None and aligulac_url not in df['url'].unique():
                    aligulac_data = get_aligulac_matches(aligulac_url)

                    aligulac_data['tier'] = tier
                    aligulac_data['url'] = aligulac_url
                    aligulac_data['tournament'] = tournament

                    df = pd.concat([df, aligulac_data]).reset_index(drop = True)
                    df.to_csv(SAVE_PATH, sep = ';', index = False)
                # end if
            # end if
            processed_tournaments.add(tournament)
            save_processed_tournaments(SAVE_PATH_TOURNAMENTS, processed_tournaments)
        # end for
    # end for
# end def
