<%
import trader.portfolio
import trader.strategy
import trader.strategy.test
import trader.plot
import trader.performance

portfolio = trader.portfolio.Portfolio()
portfolio.add_cash(10000)
strategy = trader.strategy.test.TestStrategy()
strategy.run(df, portfolio)
mtm = portfolio.mtm(df)
stats = trader.performance.summary_stats(mtm)
%>

<pre>
Culmuative return (%): ${stats['cret'] * 100.0}
Culmuative var (%): ${stats['cvar'] * 100.0}
Sharpe (%): ${stats['sharpe'] * 100.0}

${portfolio.orders}
</pre>
${trader.plot.plot_line(mtm, 'time', 'mtm')}




