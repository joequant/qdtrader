import trader.transform

def count(df):
    return df.count

def describe_stats(df):
    return trader.transform.last_price(df).describe()

