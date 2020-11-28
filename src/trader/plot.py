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

def plot_line(df, x, y):
    source = ColumnDataSource(df)
    p = figure()
    p.line(x, y, source=source)
    return file_html(p, CDN, "last plot")

def pnl_plot(df, portfolio):
    return plot_test()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def plot_animate_test():
    fig, ax = plt.subplots()
    x = np.arange(0, 2*np.pi, 0.01)
    line, = ax.plot(x, np.sin(x))

    def animate(i):
        line.set_ydata(np.sin(x + i / 50))  # update the data.
        return line,

    ani = animation.FuncAnimation(
        fig, animate, interval=20, blit=True, save_count=50)
    plt.show()
