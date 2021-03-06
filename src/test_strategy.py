#!/usr/bin/python3
import qdtrader.portfolio
import qdtrader.strategy
import qdtrader.strategy.hodl
import qdtrader.strategy.test
import qdtrader.strategy.testsignal
import qdtrader.performance
import qdtrader.data
import pandas

df =  qdtrader.data.get_data("../data/ModelDepthProto_20170125.csv")

p0 = qdtrader.portfolio.Portfolio()
p0.add_cash(10000)
strategy = qdtrader.strategy.hodl.HodlStrategy()
strategy.run(df, p0)
mtm0 = p0.mtm(df)
print(mtm0)
print(qdtrader.performance.summary_stats(mtm0))

p1 = qdtrader.portfolio.Portfolio()
p1.add_cash(10000)
strategy = qdtrader.strategy.test.TestStrategy()
strategy.run(df, p1)
mtm = p1.mtm(df)
print(mtm)
print(qdtrader.performance.summary_stats(mtm))

p2 = qdtrader.portfolio.Portfolio()
p2.add_cash(10000)
strategy = qdtrader.strategy.testsignal.TestSignalStrategy()
strategy.run(df, p2)
print(p2.orders)

