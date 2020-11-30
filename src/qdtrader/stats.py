import qdtrader.transform

def count(df):
    return df.count

def describe_stats(df):
    return qdtrader.transform.last_price(df).describe()

