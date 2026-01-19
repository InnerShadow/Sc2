import os

BASE_URL = "https://liquipedia.net"
URL = "https://liquipedia.net/starcraft2/S-Tier_Tournaments"

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

LIQUIPEDIA_URLS = [
    'https://liquipedia.net/starcraft2/S-Tier_Tournaments',
    'https://liquipedia.net/starcraft2/A-Tier_Tournaments',
    'https://liquipedia.net/starcraft2/A-Tier_Tournaments/LotV/2018-2020',
    'https://liquipedia.net/starcraft2/B-Tier_Tournaments/2025',
    'https://liquipedia.net/starcraft2/B-Tier_Tournaments/2024',
    'https://liquipedia.net/starcraft2/B-Tier_Tournaments/2023',
    'https://liquipedia.net/starcraft2/B-Tier_Tournaments/2022',
    'https://liquipedia.net/starcraft2/B-Tier_Tournaments/2021',
    'https://liquipedia.net/starcraft2/B-Tier_Tournaments/2020',
    'https://liquipedia.net/starcraft2/C-Tier_Tournaments/2025',
    'https://liquipedia.net/starcraft2/C-Tier_Tournaments/2024',
    'https://liquipedia.net/starcraft2/C-Tier_Tournaments/2023',
    'https://liquipedia.net/starcraft2/C-Tier_Tournaments/2023',
    'https://liquipedia.net/starcraft2/C-Tier_Tournaments/2021',
    'https://liquipedia.net/starcraft2/C-Tier_Tournaments/2020'
]

SAVE_PATH = os.path.join('.', 'data', 'dataset.csv')