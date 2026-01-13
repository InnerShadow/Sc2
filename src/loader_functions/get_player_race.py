import requests
from bs4 import BeautifulSoup

from src.config import HEADERS, BASE_URL, GAME

def get_player_race(player : str):
    player_url = f"{BASE_URL}/{GAME}/{player}"
    resp = requests.get(player_url, headers = HEADERS)
    soup = BeautifulSoup(resp.text, "html.parser")

    for div in soup.select("div.infobox-cell-2.infobox-description"):
        if div.get_text(strip=True).lower().startswith("race"):
            value_div = div.find_next_sibling("div")
            if value_div:
                return value_div.get_text(strip=True)
            # end if
        # end if
    # end for

    return None
# end def
