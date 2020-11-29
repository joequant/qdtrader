<%
import trader.portfolio
import trader.strategy
import trader.strategy.test
import trader.plot
import trader.performance

p1 = trader.portfolio.Portfolio()
p1.add_cash(10000)
strategy1 = trader.strategy.test.TestStrategy()
strategy1.run(df, p1)
mtm1 = p1.mtm(df)
stats1 = trader.performance.summary_stats(mtm1)
%>
<h2>Test Strategy</h2>
<pre>
Culmuative return (%): ${stats1['cret'] * 100.0}
Culmuative var (%): ${stats1['cvar'] * 100.0}
Sharpe (%): ${stats1['sharpe'] * 100.0}

${p1.orders}
</pre>
${trader.plot.plot_line(mtm1, 'time', 'mtm')}

<h2>Test Signal Strategy</h2>
<%
import trader.strategy.testsignal
p2 = trader.portfolio.Portfolio()
p2.add_cash(10000)
strategy2 = trader.strategy.testsignal.TestSignalStrategy(ratio=0.2)
strategy2.run(df, p2)
mtm2 = p2.mtm(df)
stats2 = trader.performance.summary_stats(mtm2)
%>

<pre>
Culmuative return (%): ${stats2['cret'] * 100.0}
Culmuative var (%): ${stats2['cvar'] * 100.0}
Sharpe (%): ${stats2['sharpe'] * 100.0}

${p2.orders}
</pre>
${trader.plot.plot_line(mtm2, 'time', 'mtm')}