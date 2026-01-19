import requests
from bs4 import BeautifulSoup

import pandas as pd

from src.config import HEADERS

def get_aligulac_matches(url : str) -> pd.DataFrame:
    resp = requests.get(url, headers = HEADERS) 
    soup = BeautifulSoup(resp.text, 'html.parser')

    matches = []

    for tbody in soup.select('tbody.lm'):
        for row in tbody.select('tr'):
            date_cell = row.select_one('td.lm_date')
            if not date_cell:
                continue
            date = date_cell.get_text(strip=True)

            score_match = row.select_one('td.lm_score').get_text(strip=True)
            p_score, o_score = score_match.replace('–', '-').split('-')
            p_score = int(p_score)
            o_score = int(o_score)

            pla = row.select_one('td.lm_pla')
            pla_a = pla.find('a')
            player = pla_a.get_text(strip=True)
            player_id = int(pla_a['href'].split('/')[2].split('-')[0])
            player_race = pla.find('img', alt=lambda x: x in {'P', 'T', 'Z', 'R'}).get('alt')

            plb = row.select_one('td.lm_plb')
            plb_a = plb.find('a')
            opponent = plb_a.get_text(strip=True)
            opponent_id = int(plb_a['href'].split('/')[2].split('-')[0])
            opponent_race = plb.find('img', alt=lambda x: x in {'P', 'T', 'Z', 'R'}).get('alt')

            if 'winner' in pla.get('class', []):
                winner_score, loser_score = p_score, o_score
            else:
                winner_score, loser_score = o_score, p_score
            # end if

            matches.append({
                'date': date,
                'player': player,
                'player_race': player_race,
                'player_score': winner_score if 'winner' in pla.get('class', []) else loser_score,
                'player_id': player_id,
                'opponent': opponent,
                'opponent_race': opponent_race,
                'opponent_score': loser_score if 'winner' in pla.get('class', []) else winner_score,
                'opponent_id': opponent_id,
                'score_match': score_match
            })
        # end for
    # end for

    df = pd.DataFrame(matches)
    return df
# end def
