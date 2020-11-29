<%
import trader.signal.unbalanced
import pandas
s = trader.signal.unbalanced.UnbalancedBook(0.5)
signals = s.generate(df)
%>
<pre>
${signals}
</pre>
