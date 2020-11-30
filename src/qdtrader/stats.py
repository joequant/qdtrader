import qdtrader.transform

def count(df):
    return df.count

def describe_stats(df):
    return df.price_ticks().describe()

