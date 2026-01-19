from tqdm import tqdm
import os
import time

import pandas as pd
import numpy as np

from src.loader_functions.get_liquipedia_tournaments import get_liquipedia_tournaments
from src.loader_functions.get_liquipedia_tornament_info import get_liquipedia_tornament_info
from src.loader_functions.get_aligulac_matches import get_aligulac_matches

from src.config import LIQUIPEDIA_URLS, SAVE_PATH

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

    for url in LIQUIPEDIA_URLS:
        print(f'start : {url}')
        tournaments = get_liquipedia_tournaments(url)
        time.sleep(60 + np.random.uniform(10, 30))
        for tournament in tqdm(tournaments):
            if tournament not in df['url'].tolist():
                tier, aligulac_url = get_liquipedia_tornament_info(tournament)
                if aligulac_url is not None and aligulac_url not in df['url'].unique():
                    aligulac_data = get_aligulac_matches(aligulac_url)
                    time.sleep(60 + np.random.uniform(10, 30))

                    aligulac_data['tier'] = tier
                    aligulac_data['url'] = aligulac_url

                    df = pd.concat([df, aligulac_data]).reset_index(drop = True)
                    df.to_csv(SAVE_PATH, sep = ';', index = False)
                # end if
            # end if
        # end for
    # end for
# end def