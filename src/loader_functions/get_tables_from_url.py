import requests
from bs4 import BeautifulSoup

from src.config import HEADERS

def get_tables_from_url(url):
    resp = requests.get(url, headers = HEADERS)
    soup = BeautifulSoup(resp.text, "html.parser")
    tables = soup.find_all("table", class_="wikitable")
    
    data = []
    for table in tables:
        rows = table.find_all("tr")[1:]
        for r in rows:
            cols = [c.get_text(strip=True) for c in r.find_all("td")]
            if cols:
                data.append(cols)
            # end if
        # end for
    # end for
    return data
# end def
