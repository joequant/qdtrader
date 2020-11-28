import bokeh
from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import file_html
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from bokeh.models.tools import HoverTool
from bokeh.embed import file_html
from bokeh.resources import CDN
import trader.transform

def plot_test():
    plot = figure()
    plot.circle([1,2], [3,4])
    return file_html(plot, CDN, "my plot")

def plot_last_price(df):
    source = ColumnDataSource(trader.transform.last_price(df))
    p = figure()
    p.line('timestampNano', 'lastPrice', source=source)
    return file_html(p, CDN, "last plot")

