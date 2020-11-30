<%
import qdtrader.plot
import qdtrader.signal.unbalanced
import pandas
s = qdtrader.signal.unbalanced.UnbalancedBook(0.5)
signals = s.generate(df)

%>
<pre>
${signals}
</pre>

${qdtrader.plot.plot_last_price(df)}
