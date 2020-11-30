#!/usr/bin/python3
import qdtrader.signal.unbalanced
import pandas

df =  pandas.read_csv("../data/ModelDepthProto_20170125.csv", index_col=1)
signal = qdtrader.signal.unbalanced.UnbalancedBook(0.5)
print(signal.generate(df))

