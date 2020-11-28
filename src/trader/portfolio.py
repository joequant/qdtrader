import pandas

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
    def orders(self):
        return self.orders
    def cash(self):
        return self.positions[self._cash]
    def position(self, product):
        return self.positions.get(product, 0)
