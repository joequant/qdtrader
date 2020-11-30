from qdtrader.signal import Signal
import pandas

class UnbalancedBook(Signal):
    def __init__(self, ratio):
        self.ratio = ratio
    def generate(self, df):
        dict_list = []
        prev_ask1p = None
        prev_bid1p = None
        for row in df.iter_price_tuples():
            (time, symbol, lastPrice, lastQty)  = df.tuple_to_tick(row)
            (ask1p, ask1q) = df.tuple_to_ask(row, 1)
            (bid1p, bid1q) = df.tuple_to_bid(row, 1)
            if ask1q == 0 or bid1q == 0:
                continue
            if prev_ask1p is not None and ask1p == prev_ask1p:
                continue
            if prev_bid1p is not None and bid1p == prev_bid1p:
                continue
            prev_ask1p = ask1p
            prev_bid1p = bid1p
            if ask1q > (1.0 + self.ratio) * bid1q:
                dict_list.append((time, 'unbalanced', 'ask',  bid1q / ask1q))
            elif bid1q > (1.0 + self.ratio)  * ask1q:
                dict_list.append((time, 'unbalanced', 'bid',  ask1q / bid1q))
        return pandas.DataFrame(dict_list, columns=['time', 'signal', 'param1', 'param2'])
