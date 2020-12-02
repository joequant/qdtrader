import qdtrader.transform
import math

def stats(df):
    pass

def summary_stats(mtm):
    try:
        cret = (mtm.iloc[-1]['mtm'] - mtm.iloc[0]['mtm']) / mtm.iloc[0]['mtm']
        cvar = mtm.var()['mtm']
        return {
            "cret": cret,
            "cvar": cvar,
            "sharpe": cret/math.sqrt(cvar)
        }
    except:
        return {
            "cret": 0.0,
            "cvar": 0.0,
            "sharpe": 0.0
            }

