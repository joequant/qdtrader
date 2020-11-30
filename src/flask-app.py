#!/usr/bin/python3
from flask import Flask
app = Flask(__name__)
from mako.template import Template
import sys
import qdtrader.data
import os
import logging

script_dir = os.path.dirname(os.path.realpath(__file__))

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route("/qdtrader/<template>/<data>")
def show_template_data(template, data):
    df = qdtrader.data.CSVDataFrame(os.path.join(script_dir, "..",
                                                 "data", data + ".csv"))
    template = Template(filename=os.path.join(script_dir, "..",
                                              "templates",
                                              template + ".mako"))
    return(template.render(df=df))

if __name__ == '__main__':
    app.run(host='0.0.0.0')
