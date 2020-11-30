#!/usr/bin/python3
import qdtrader.signal.unbalanced
import qdtrader.data
import pandas

df =  qdtrader.data.CSVDataFrame("../data/ModelDepthProto_20170125.csv")
signal = qdtrader.signal.unbalanced.UnbalancedBook(0.5)
print(signal.generate(df))

