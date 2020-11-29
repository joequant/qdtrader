from trader.strategy import Strategy
import trader.transform

class HodlStrategy(Strategy):
    def __init__(self):
        super().__init__()
        self.reflevel = None
    def run(self, df, portfolio):
        pass
