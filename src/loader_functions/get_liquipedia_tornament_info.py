import requests
from bs4 import BeautifulSoup

from src.config import HEADERS

def get_liquipedia_tornament_info(url : str) -> str:
    resp = requests.get(url, headers = HEADERS)
    soup = BeautifulSoup(resp.text, 'html.parser')

    aligulac_url = None

    a = soup.select_one('a:has(i.lp-aligulac)')
    if a:
        aligulac_url = a['href']
    # end if

    return aligulac_url
# end def
