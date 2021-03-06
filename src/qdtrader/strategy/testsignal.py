from qdtrader.strategy import Strategy
from qdtrader.signal.unbalanced import UnbalancedBook; 
import qdtrader.transform

class TestSignalStrategy(Strategy):
    def __init__(self, ratio=0.2, purchase_ratio=0.5):
        super().__init__()
        self.reflevel = None
        self.purchase_ratio = purchase_ratio
        self.signal_generator = UnbalancedBook(ratio)
    def run(self, df, portfolio):
        signals = self.signal_generator.generate(df)
        signal_iter = signals.iterrows()
        try:
            i1 = signal_iter.__next__()[1]
        except StopIteration:
            return
        prev_time = None
        for row in df.price_ticks().itertuples():
            (time, symbol, price, quantity) = row[0:4]
            if i1 is None:
                return
            if time == i1['time'] or (prev_time is not None and \
                                      prev_time < i1['time'] and i1['time'] < time):
                if i1['param1'] == "bid":
                    portfolio.buy(symbol, portfolio.cash() \
                                  * self.purchase_ratio / price,
                                  price, time)
                else:
                    portfolio.sell(symbol, portfolio.position(symbol) \
                                   * self.purchase_ratio,
                                   price, time)
            while i1 is not None and i1['time'] < time:
                try:
                    i1 = signal_iter.__next__()[1]                    
                except StopIteration:
                    i1 = None
            prev_time = time

