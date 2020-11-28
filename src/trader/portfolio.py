import pandas

class Portfolio:
    def __init__(self, cash='USD', **kwargs):
        self._cash = cash
        self.positions = kwargs
        self.positions[self._cash] = 0
        self.orders = pandas.DataFrame(columns=['time', 'type', 'product', 'amount', 'price'])
    def add_cash(self, cash_to_add):
        self.positions[self._cash] += cash_to_add
    def buy(self, product, amount, price, time):
        self.positions[product] = self.positions.get(product, 0) + amount
        self.positions[self._cash] = self.positions.get(self._cash, 0) - amount * price
        self.orders = self.orders.append({'time': time,
                            'type': 'buy',
                            'product': product,
                            'amount': amount,
                            'price': price},
                           ignore_index=True)

    def sell(self, product, amount, price, time):
        self.positions[product] = self.positions.get(product, 0) - amount
        self.positions[self._cash] = self.positions.get(self._cash, 0) + amount * price
        self.orders = self.orders.append({'time': time,
                            'type': 'sell',
                            'product': product,
                            'amount': amount,
                            'price': price},
                           ignore_index=True)
    def orders(self):
        return self.orders
    def cash(self):
        return self.positions[self._cash]
    def position(self, product):
        return self.positions.get(product, 0)

