<%
import trader.plot
%>

${trader.plot.plot_last_price(df)}
${trader.plot.plot_order_book_animation(df, 0, 2000)}
