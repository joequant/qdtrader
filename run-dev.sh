#!/bin/bash
PYTHONPATH=`pwd`/src
src/generate_report.py data/ModelDepthProto_20170125.csv out  templates/strategy.mako

