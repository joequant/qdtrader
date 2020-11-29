from trader.strategy import Strategy
import trader.transform

class HodlStrategy(Strategy):
    def __init__(self):
        super().__init__()
        self.reflevel = None
    def run(self, df, portfolio):
        symbol = df.iloc[0][0]
        time = df.iloc[0][1]
        price = df.iloc[0][2]
        portfolio.buy(symbol, portfolio.cash() / price,
                      price, time)
        pass
