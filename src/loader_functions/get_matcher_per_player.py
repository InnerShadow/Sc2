import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin
import time

from src.loader_functions.get_tables_from_url import get_tables_from_url
from src.loader_functions.parse_liquipedia_datetime import parse_liquipedia_datetime
from src.loader_functions.extract_tier import extract_tier
from src.config import BASE_URL, GAME, HEADERS, REPLACE_WINS_DICT

def get_matcher_per_player(player_name : str):
    player_url = f"{BASE_URL}/{GAME}/{player_name}/Matches"
    all_matches = get_tables_from_url(player_url)

    resp = requests.get(player_url, headers=HEADERS)
    soup = BeautifulSoup(resp.text, "html.parser")
    links = soup.find_all("a")

    season_links = set()
    for a in links:
        href = a.get("href")
        if href and "Matches" in href and href != f"/{GAME}/{player_name}/Matches":
            full_url = urljoin(BASE_URL, href)
            season_links.add(full_url)
        # end if
    # end for

    for link in season_links:
        try:
            all_matches.extend(get_tables_from_url(link))
            time.sleep(30)
        except Exception as e:
            print("Error:", e)
        # end try
    # end for

    df = pd.DataFrame(all_matches)
    df.columns = ('date', 'match', 'skip1', 'tournament', 'player', 'score', 'oponent', 'skip2')
    df = df.drop(columns = ['skip1', 'skip2'])

    df = df[df['player'] == player_name].reset_index(drop = True)

    df['date'] = parse_liquipedia_datetime(df['date'])
    df['date'] = df['date'].fillna(pd.to_datetime('2100-01-01', format = '%Y-%m-%d'))

    df['player_wins'] = df['score'].apply(lambda x : x.split(':')[0].strip())
    df['oponent_wins'] = df['score'].apply(lambda x : x.split(':')[-1].strip())
    df[['player_wins', 'oponent_wins']] = df[['player_wins', 'oponent_wins']].replace(REPLACE_WINS_DICT)
    df[['player_wins', 'oponent_wins']] = df[['player_wins', 'oponent_wins']].astype(int)
    df['best_of'] = (
        df[['player_wins', 'oponent_wins']].max(axis = 1)
            .pipe(lambda s: s + 1 + (s % 2))
    )
    df.loc[(df['player_wins'] + df['oponent_wins']) == 1, 'best_of'] = 1

    df = df[df['date'] >= pd.to_datetime('2020-01-01', format = '%Y-%m-%d')]

    df['tournament_tier'] = extract_tier(df['match'])

    df = df.drop(columns = ('score'))

    series_list = []
    for row in df.iterrows():
        row_tmp = row[1].copy()
        row_tmp['player'], row_tmp['oponent'] = row_tmp['oponent'], row_tmp['player']
        row_tmp['player_wins'], row_tmp['oponent_wins'] = row_tmp['oponent_wins'], row_tmp['player_wins']

        series_list.append(row_tmp)
    # end for

    df_tmp = pd.DataFrame(series_list)
    df = pd.concat([df, df_tmp]).reset_index(drop = True)

    df["target"] = (df["player_wins"] > df["oponent_wins"]).astype(int)
    
    return df
# end def
