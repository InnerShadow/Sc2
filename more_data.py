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

if __name__ == '__main__':

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

    for tournament, tier in tqdm(zip(['https://liquipedia.net/starcraft2/Thunderfire_SC2_Allstar/2025',
                                      'https://liquipedia.net/starcraft2/OSC_Championship_13',
                                      'https://liquipedia.net/starcraft2/Rising_Star_Cup/1'
                                      'https://liquipedia.net/starcraft2/Chicken_King_Cup/8',
                                      'https://liquipedia.net/starcraft2/OSC_King_of_the_Hill_Weekly/235',
                                      'https://liquipedia.net/starcraft2/The_Berry_Patch_Open',
                                      'https://liquipedia.net/starcraft2/Basilisk_Big_Brain_Bouts/104',
                                      'https://liquipedia.net/starcraft2/PiGosaur_Cup/65',
                                      'https://liquipedia.net/starcraft2/Thunderfire_SC2_Allstar/2025',
                                      'https://liquipedia.net/starcraft2/Monday_Night_Weeklies/37',
                                      'https://liquipedia.net/starcraft2/WardiTV_Mondays/71',
                                      'https://liquipedia.net/starcraft2/The_5.4k_Patch_Clash/12',
                                      'https://liquipedia.net/starcraft2/PiGosaur_Cup/64',
                                      'https://liquipedia.net/starcraft2/WardiTV_Mondays/69',
                                      'https://liquipedia.net/starcraft2/Monday_Night_Weeklies/36',
                                      'https://liquipedia.net/starcraft2/Soop_invitational',
                                      'https://liquipedia.net/starcraft2/Elpis_Invitational/2026/Winter',
                                      'https://liquipedia.net/starcraft2/PiGosaur_Cup/63',
                                      'https://liquipedia.net/starcraft2/Mini_Rotti_Monday/2',
                                      'https://liquipedia.net/starcraft2/WardiTV_Mondays/68',
                                      'https://liquipedia.net/starcraft2/Patch_Clash_Invitational/1',
                                      'https://liquipedia.net/starcraft2/Platinum_StarCraft_2_League/Season_Finals',
                                      'https://liquipedia.net/starcraft2/Hungarian_Pro_Series/Telapo_Cup',
                                      'https://liquipedia.net/starcraft2/The_5.4k_Patch_Clash/10',
                                      'https://liquipedia.net/starcraft2/Korean_Starcraft_League/84',
                                      'https://liquipedia.net/starcraft2/Sunrise_Cup/2025_Grand_Finals'],
                                     ['S', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'
                                      'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'])):
        if tournament in processed_tournaments:
            continue
        # end if
        aligulac_url = get_liquipedia_tornament_info(tournament)
        # print(f'{aligulac_url} FROM {tournament}')
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