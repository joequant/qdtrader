from qdtrader.strategy import Strategy
import qdtrader.transform

class HodlStrategy(Strategy):
    def __init__(self):
        super().__init__()
        self.reflevel = None
    def run(self, df, portfolio):
        (time, symbol, price, quantity) = df.nth_price_tick(0)
        portfolio.buy(symbol, portfolio.cash() / price,
                      price, time)
        pass
