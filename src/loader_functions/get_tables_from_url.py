import requests
from bs4 import BeautifulSoup
import numpy as np
import time

from src.config import HEADERS

def get_tables_from_url(url : str, trys : int = 0, need_retry : bool = False):
    resp = requests.get(url, headers = HEADERS, timeout = 60)
    soup = BeautifulSoup(resp.text, "html.parser")
    tables = soup.find_all("table", class_="wikitable")
    print(f'{url} : {resp.status_code} ===== {resp if resp.status_code > 300 else ""}')

    if resp.status_code > 300 and trys < 2 and need_retry:
        print(f'retry : {url} {trys + 1} trys')
        time.sleep(np.random.uniform(10, 120))
        get_tables_from_url(url, trys + 1, need_retry)
    # end if
    
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
