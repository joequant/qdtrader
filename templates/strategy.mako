<%
import trader.portfolio
import trader.strategy
import trader.strategy.test
import trader.plot

portfolio = trader.portfolio.Portfolio()
portfolio.add_cash(10000)
strategy = trader.strategy.test.TestStrategy()
strategy.run(df, portfolio)
mtm = portfolio.mtm(df)
%>

<pre>
${portfolio.orders}
</pre>
${trader.plot.plot_line(mtm, 'time', 'mtm')}



