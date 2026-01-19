
import json
import os

def load_processed_tournaments(path: str) -> set:
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        # end with
        return set(data.get('tournaments', []))
    # end if
    return set()
# end def


def save_processed_tournaments(path: str, tournaments: set):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(
            {'tournaments': sorted(tournaments)},
            f,
            ensure_ascii=False,
            indent=2
        )
    # end with
# end def

