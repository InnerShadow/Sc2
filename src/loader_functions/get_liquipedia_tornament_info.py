import requests
from bs4 import BeautifulSoup

from typing import Tuple

from src.config import HEADERS

def get_liquipedia_tornament_info(url : str) -> Tuple[str, str]:
    resp = requests.get(url, headers = HEADERS)
    soup = BeautifulSoup(resp.text, 'html.parser')

    tier = None

    tier_block = soup.select_one('div.valvepremier-highlighted')
    if tier_block:
        a = tier_block.find('a')
        if a:
            tier = a.get_text(strip=True)
        # end if
    # end if

    aligulac_url = None

    a = soup.select_one('a:has(i.lp-aligulac)')
    if a:
        aligulac_url = a['href']
    # end if

    return tier, aligulac_url
# end def
