import os

BASE_URL = "https://liquipedia.net"
URL = "https://liquipedia.net/starcraft2/S-Tier_Tournaments"

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

LIQUIPEDIA_URLS = {
    'https://liquipedia.net/starcraft2/S-Tier_Tournaments' : 'S',
    'https://liquipedia.net/starcraft2/A-Tier_Tournaments' : 'A',
    # 'https://liquipedia.net/starcraft2/A-Tier_Tournaments/LotV/2018-2020' : 'A',
    'https://liquipedia.net/starcraft2/B-Tier_Tournaments/2025' : 'B',
    'https://liquipedia.net/starcraft2/B-Tier_Tournaments/2024' : 'B',
    'https://liquipedia.net/starcraft2/B-Tier_Tournaments/2023' : 'B',
    'https://liquipedia.net/starcraft2/B-Tier_Tournaments/2022' : 'B',
    'https://liquipedia.net/starcraft2/B-Tier_Tournaments/2021' : 'B',
    'https://liquipedia.net/starcraft2/B-Tier_Tournaments/2020' : 'B',
    # 'https://liquipedia.net/starcraft2/C-Tier_Tournaments/2025' : 'C',
    # 'https://liquipedia.net/starcraft2/C-Tier_Tournaments/2024' : 'C',
    # 'https://liquipedia.net/starcraft2/C-Tier_Tournaments/2023' : 'C',
    # 'https://liquipedia.net/starcraft2/C-Tier_Tournaments/2023' : 'C',
    # 'https://liquipedia.net/starcraft2/C-Tier_Tournaments/2021' : 'C',
    # 'https://liquipedia.net/starcraft2/C-Tier_Tournaments/2020' : 'C'
}

SAVE_PATH = os.path.join('.', 'data', 'dataset.csv')
SAVE_PATH_TOURNAMENTS = os.path.join('.', 'data', 'tournaments.json')
