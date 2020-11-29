#!/usr/bin/python3
import trader.portfolio
import trader.strategy
import trader.strategy.hodl
import trader.strategy.test
import trader.strategy.testsignal
import trader.performance
import pandas

df =  pandas.read_csv("../data/ModelDepthProto_20170125.csv")

p0 = trader.portfolio.Portfolio()
p0.add_cash(10000)
strategy = trader.strategy.hodl.HodlStrategy()
strategy.run(df, p0)
mtm0 = p0.mtm(df)
print(mtm0)
print(trader.performance.summary_stats(mtm0))

p1 = trader.portfolio.Portfolio()
p1.add_cash(10000)
strategy = trader.strategy.test.TestStrategy()
strategy.run(df, p1)
mtm = p1.mtm(df)
print(mtm)
print(trader.performance.summary_stats(mtm))

p2 = trader.portfolio.Portfolio()
p2.add_cash(10000)
strategy = trader.strategy.testsignal.TestSignalStrategy()
strategy.run(df, p2)
print(p2.orders)

