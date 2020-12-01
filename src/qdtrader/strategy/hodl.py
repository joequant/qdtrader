from qdtrader.strategy import Strategy
import qdtrader.transform

class HodlStrategy(Strategy):
    def __init__(self):
        super().__init__()
        self.reflevel = None
    def run(self, df, portfolio):
        i = df.price_ticks().itertuples()
        (time,symbol,price,quantity) = i.__next__()[0:4]
        portfolio.buy(symbol, portfolio.cash() / price,
                      price, time)
        pass
