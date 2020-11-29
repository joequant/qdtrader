#!/usr/bin/python3
import trader.signal.unbalanced
import pandas

df =  pandas.read_csv("../data/ModelDepthProto_20170125.csv")
signal = trader.signal.unbalanced.UnbalancedBook(0.5)
print(signal.generate(df))
