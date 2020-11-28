def last_price(df):
    return df.loc[df['lastPrice'] > 0]

def mark_to_market(df, portfolio):
    return df.loc[df['lastPrice'] > 0]

