<%
import qdtrader.portfolio
import qdtrader.strategy
import qdtrader.strategy.test
import qdtrader.plot
import qdtrader.performance

p1 = qdtrader.portfolio.Portfolio()
p1.add_cash(10000)
strategy1 = qdtrader.strategy.test.TestStrategy()
strategy1.run(df, p1)
mtm1 = p1.mtm(df)
stats1 = qdtrader.performance.summary_stats(mtm1)
%>


<h2>Test Hodl</h2>
<%
import qdtrader.strategy.hodl
p0 = qdtrader.portfolio.Portfolio()
p0.add_cash(10000)
strategy0 = qdtrader.strategy.hodl.HodlStrategy()
strategy0.run(df, p0)
mtm0 = p0.mtm(df)
stats0 = qdtrader.performance.summary_stats(mtm0)
%>

<pre>
Culmuative return (%): ${stats0['cret'] * 100.0}
Culmuative var (%): ${stats0['cvar'] * 100.0}
Sharpe (%): ${stats0['sharpe'] * 100.0}

${p0.orders}
</pre>
${qdtrader.plot.plot_line(mtm0, 'time', 'mtm')}

<h2>Test Strategy</h2>
<pre>
Culmuative return (%): ${stats1['cret'] * 100.0}
Culmuative var (%): ${stats1['cvar'] * 100.0}
Sharpe (%): ${stats1['sharpe'] * 100.0}

${p1.orders}
</pre>
${qdtrader.plot.plot_line(mtm1, 'time', 'mtm')}

<h2>Test Signal Strategy</h2>
<%
import qdtrader.strategy.testsignal
p2 = qdtrader.portfolio.Portfolio()
p2.add_cash(10000)
strategy2 = qdtrader.strategy.testsignal.TestSignalStrategy(ratio=0.2)
strategy2.run(df, p2)
mtm2 = p2.mtm(df)
stats2 = qdtrader.performance.summary_stats(mtm2)
%>

<pre>
Culmuative return (%): ${stats2['cret'] * 100.0}
Culmuative var (%): ${stats2['cvar'] * 100.0}
Sharpe (%): ${stats2['sharpe'] * 100.0}

${p2.orders}
</pre>
${qdtrader.plot.plot_line(mtm2, 'time', 'mtm')}