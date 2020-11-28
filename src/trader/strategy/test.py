from trader.strategy import Strategy

def TestStrategy(Strategy):
    def __init__(self):
        self.reflevel = None
    def run(self, data, portfolio):
        for index, row in df.iterrows():
            if row['lastPrice'] != 0:
                if self.reflevel is not None:
                    self.reflevel = row['lastPrice']

