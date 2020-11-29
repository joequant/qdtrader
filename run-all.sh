#!/bin/bash
for i in data/*.csv ; do
    echo $i
    src/generate_report.py $i out templates/plots.mako templates/hello_world.mako templates/plot_pandas.mako templates/stats.mako templates/strategy.mako templates/signal.mako
done
