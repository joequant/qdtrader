from qdtrader.strategy import Strategy
import qdtrader.transform

class TestStrategy(Strategy):
    def __init__(self):
        super().__init__()
        self.reflevel = None
    def run(self, df, portfolio):
        for row in df.iter_price_tuples():
            (time, symbol, price, quantity) = df.tuple_to_tick(row)
            if self.reflevel is None:
                self.reflevel = price
            if price > 1.005 * self.reflevel:
                portfolio.sell(symbol, portfolio.position(symbol) * 0.5,
                               price, time)
                self.reflevel = price
            elif price < 0.9995 * self.reflevel:
                portfolio.buy(symbol, portfolio.cash() * 0.5 / price,
                              price, time)
                self.reflevel = price

                                   
