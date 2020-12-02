import pandas
import qdtrader.transform
import os

class Data:
    def __init__(self):
        pass

class ModelDepthProtoDataFrame(Data):
    def __init__(self, filename, index_col=1):
        self._dataframe = pandas.read_csv(filename, index_col=1)
    def df(self):
        return self._dataframe
    def itertuples(self):
        return self._dataframe.itertuples()
    def tuple_to_ask(self, row, depth=1):
        return (row[3+depth], row[4+depth])
    def tuple_to_bid(self, row, depth=1):
        return (row[13+depth], row[14+depth])
    @property
    def count(self):
        return self._dataframe.count
    def price_ticks(self):
        df = qdtrader.transform.last_price(self._dataframe)
        df.index.names = ["time"]
        df = df.rename(columns={
            df.columns[0]: "symbol",
            df.columns[1]: "price",
            df.columns[2]: "qty"
        })
        return df

class CryptoDownload(Data):
    def __init__(self, filename, index_col=1):
        self._dataframe = pandas.read_csv(filename, index_col=0,skiprows=1)
    def df(self):
        return self._dataframe
    def itertuples(self):
        return self._dataframe.itertuples()
    def tuple_to_ask(self, row, depth=1):
        return (None, None)
    def tuple_to_bid(self, row, depth=1):
        return (None, None)
    @property
    def count(self):
        return self._dataframe.count
    def price_ticks(self):
        df = self.df().loc[:,['Symbol','Close','Volume BTC']]
        df.index.names = ["time"]
        df = df.rename(columns={
            df.columns[0]: "symbol",
            df.columns[1]: "price",
            df.columns[2]: "qty"
        })
        return df

def get_data(filename):
    basename = os.path.basename(filename)
    if "ModelDepthProto" in basename:
        return ModelDepthProtoDataFrame(filename)
    elif "Binance" in basename:
        return CryptoDownload(filename)
