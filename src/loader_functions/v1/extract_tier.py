import pandas as pd

def extract_tier(s: pd.Series) -> pd.Series:
    tier = s.str.extract(r'\(([SABC])\)', expand=False)

    tier = tier.fillna(
        s.str.extract(r'\b([SABC])\s*-?\s*Tier\b', expand=False)
    )

    return tier
# end def
