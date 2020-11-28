<%
import trader.portfolio
import trader.strategy
import trader.strategy.test

portfolio = trader.portfolio.Portfolio()
portfolio.add_cash(10000)
strategy = trader.strategy.test.TestStrategy()
strategy.run(df, portfolio)
%>

${portfolio.orders}

