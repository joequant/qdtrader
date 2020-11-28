#!/bin/bash
PYTHONPATH=`pwd`/src
src/generate_report.py templates/plots.mako  data/ModelDepthProto_20170125.csv > out/plot_pandas.html


