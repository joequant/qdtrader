#!/usr/bin/python3
from mako.template import Template
import sys
import pandas
import os
import logging
#print(sys.argv[1])
#print(sys.argv[2])
logging.info("reading " + sys.argv[1])
df = pandas.read_csv(sys.argv[1])
logging.info("done reading")
dir = sys.argv[2]
for i in sys.argv[3:]:
    logging.info("reading template " + sys.argv[1])
    template = Template(filename=i)
    with open(os.path.join(dir, os.path.basename(i).rsplit('.', 1)[0] + '.html'), "w") as f:
        print(template.render(df=df), file=f)
    logging.info("finished template")