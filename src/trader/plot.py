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
    return ani.to_jstml()

def plot_order_book_animation(df, count1=None, count2=None):
    fig, ax = plt.subplots()
    askx = []
    asky = []
    bidx = []
    bidy = []
    count = 0
    for row in df.itertuples():
        time = row[2]
        if count1 is not None and count < count1:
            count = count+1
            continue
        if count2 is not None and count > count2:
            count = count+1
            continue
        askx_item = [row[5], row[7], row[9], row[11], row[13]]
        asky_item = [row[6], row[8], row[10], row[12], row[14]]
        bidx_item = [row[15], row[17], row[19], row[21], row[23]]
        bidy_item = [row[16], row[18], row[20], row[22], row[24]]
        bidy_citem = [sum(bidy_item[0:x]) for x in range(0, len(bidy_item))]
        asky_citem = [sum(asky_item[0:x]) for x in range(0, len(asky_item))]

        askx.append(askx_item)
        asky.append(asky_citem)
        bidx.append(bidx_item)
        bidy.append(bidy_citem)
        count = count+1

    print(len(askx))
    line1, = ax.plot(askx[0], asky[0])
    line2, = ax.plot(bidx[0], bidy[0])

    def animate(i):
        line1.set_xdata(askx[i])
        line1.set_ydata(asky[i])
        line2.set_xdata(bidx[i])
        line2.set_ydata(bidy[i])

    ani = animation.FuncAnimation(
        fig, animate, interval=20, frames=len(askx)-1)

    return ani.to_jshtml()
