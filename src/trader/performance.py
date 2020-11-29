import trader.transform

def stats(df):
    pass

def summary_stats(mtm):
    cret = (mtm.iloc[-1]['mtm'] - mtm.iloc[0]['mtm']) / mtm.iloc[0]['mtm']
    cvar = mtm.var()['mtm']
    return {
        "cret": cret,
        "cvar": cvar,
        "sharpe": cret/cvar
        }
