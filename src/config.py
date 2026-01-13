import os

HEADERS = {"User-Agent": "Mozilla/5.0"}
BASE_URL = "https://liquipedia.net"
GAME = "starcraft2"

REPLACE_WINS_DICT = {
    'W' : 1,
    'L' : 0,
    '' : 0,
    'FF' : 0
}

PATH_TO_PLAYERS = os.path.join('.', 'data', 'players.csv')