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
        links = cell.find_all('a', href=True)
        if not links:
            continue
        # end if

        a = links[-1]

        tournament_links.append(
            urljoin(BASE_URL, a['href'])
        )
    # end for

    return tournament_links
# end def
