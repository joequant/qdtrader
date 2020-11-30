import pandas
import qdtrader.transform

class Portfolio:
    def __init__(self, cash='USD', **kwargs):
        self._cash = cash
        self.positions = kwargs
        self.positions[self._cash] = 0
        self.orders = pandas.DataFrame(columns=['time', 'type', 'product', 'amount', 'price'])
        self.position_history = pandas.DataFrame(columns=['time',
                                                          self._cash])
    def add_cash(self, cash_to_add, time=None):
        self.positions[self._cash] += cash_to_add
        if time is not None:
            self.add_position_history(time)
    def buy(self, product, amount, price, time):
        self.positions[product] = self.positions.get(product, 0) + amount
        self.positions[self._cash] = self.positions.get(self._cash, 0) - amount * price
        self.orders = self.orders.append({'time': time,
                            'type': 'buy',
                            'product': product,
                            'amount': amount,
                            'price': price},
                           ignore_index=True)
        self.add_position_history(time)        

    def sell(self, product, amount, price, time):
        self.positions[product] = self.positions.get(product, 0) - amount
        self.positions[self._cash] = self.positions.get(self._cash, 0) + amount * price
        self.orders = self.orders.append({'time': time,
                            'type': 'sell',
                            'product': product,
                            'amount': amount,
                            'price': price},
                           ignore_index=True)
        self.add_position_history(time)
    def add_position_history(self, time):
        d = self.positions.copy()
        d['time'] = time
        self.position_history = \
            self.position_history.append(d,
                                         ignore_index=True)
    def cash(self):
        return self.positions[self._cash]
    def position(self, product):
        return self.positions.get(product, 0)
    def mtm(self, df):
        mtm_list = []
        i = self.position_history.iterrows()
        i1 = i.__next__()[1]
        try:
            i2 = i.__next__()[1]
        except StopIteration:
            i2 = None
        for row in df.price_ticks().itertuples():
            (time, symbol, price, quantity) = row[0:4]
            if time < i1['time']:
                continue
            while i2 is not None and time >= i2['time']:
                try:
                    i1 = i2
                    i2 = i.__next__()[1]
                except StopIteration:
                    i1 = i2
                    i2 = None
            mtm_list.append((time, i1[self._cash] + \
                             i1[symbol] * price))
        return pandas.DataFrame(mtm_list, columns=['time', 'mtm'])
