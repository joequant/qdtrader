#!/bin/bash
PYTHONPATH=`pwd`/src
src/generate_report.py data/ModelDepthProto_20170125.csv out  templates/strategy.mako templates/plots_animate.mako templates/signal.mako

#src/generate_report.py data/ModelDepthProto_20170125.csv out  templates/plot_pandas.mako




