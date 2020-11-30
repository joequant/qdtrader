import pandas
import qdtrader.transform

class Data:
    def __init__(self):
        pass

class CSVDataFrame(Data):
    def __init__(self, filename, index_col=1):
        self._dataframe = pandas.read_csv(filename, index_col=1)
    def df():
        return self._dataframe
    def nth_price_tick(self, i):
        row = self._dataframe.iloc[i]
        return (row.name, row[0], row[1], row[2])
    def price_rows(self):
        pass
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

