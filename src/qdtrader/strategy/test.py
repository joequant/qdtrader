from qdtrader.strategy import Strategy
import qdtrader.transform

class TestStrategy(Strategy):
    def __init__(self):
        super().__init__()
        self.reflevel = None
    def run(self, df, portfolio):
        df = qdtrader.transform.last_price(df)
        for row in df.itertuples():
            symbol = row[1]
            time = row[0]
            price =  row[2]
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

                                   
