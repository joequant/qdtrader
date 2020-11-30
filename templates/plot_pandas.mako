<%
import qdtrader.plot
%>

${qdtrader.plot.plot_last_price(df)}
${qdtrader.plot.plot_order_book_animation(df, 0, 2000)}
