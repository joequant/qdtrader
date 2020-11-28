def last_price(df):
    return df.loc[df['lastPrice'] > 0]
