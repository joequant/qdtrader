from qdtrader.signal import Signal
import pandas

class UnbalancedBook(Signal):
    def __init__(self, ratio):
        self.ratio = ratio
    def generate(self, df):
        dict_list = []
        prev_ask1p = None
        prev_bid1p = None
        for row in df.itertuples():
            time  = row[0]
            lastPrice = row[2]
            lastQty = row[3]
            ask1p = row[4]
            ask1q = row[5]
            bid1p = row[14]
            bid1q = row[15]
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
