import pandas as pd

def parse_liquipedia_datetime(s: pd.Series) -> pd.Series:
    try:
        s = s.str.replace(
            r'(UTC|CET|CEST|KST|EDT|CDT|CST|EST|PDT)$',
            '',
            regex=True
        ).str.strip()

        s = s.str.replace(r'\s*-\s*\d{1,2}:\d{2}$', '', regex=True)

        return pd.to_datetime(s, format='mixed', errors='coerce').dt.normalize()
    except AttributeError as e:
        return pd.to_datetime('2020-01-01', format='mixed', errors='coerce').dt.normalize()
    # end try
# end def
