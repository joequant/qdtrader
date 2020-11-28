#!/usr/bin/python3
import trader.portfolio
import trader.strategy
import trader.strategy.test
import pandas

df =  pandas.read_csv("../data/ModelDepthProto_20170125.csv")
portfolio = trader.portfolio.Portfolio()
portfolio.add_cash(10000)
strategy = trader.strategy.test.TestStrategy()
strategy.run(df, portfolio)
print(portfolio.mtm(df))

