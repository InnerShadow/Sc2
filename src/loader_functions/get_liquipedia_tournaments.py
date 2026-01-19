import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

from typing import List

from src.config import HEADERS, BASE_URL

def get_liquipedia_tournaments(url : str) -> List[str]:
    resp = requests.get(url, headers = HEADERS)
    soup = BeautifulSoup(resp.text, 'html.parser')
    
    tournament_links = []

    for cell in soup.select('div.gridCell.Tournament.Header'):
        a = cell.find('a', href=True)
        if a:
            tournament_links.append(
                urljoin(BASE_URL, a['href'])
            )
        # end if
    # end for

    return tournament_links
# end def
