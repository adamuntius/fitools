import yfinance as yf
import matplotlib.pyplot as plt

def dividend_plot(ticker_list):
    for ticker in ticker_list:
        data = yf.Ticker(ticker)
        div = data.dividends
        x_p = div.index
        y_p = div.values
        plt.plot(x_p, y_p)
    plt.show()

def price_plot(ticker_list):
    for ticker in ticker_list:
        data = yf.Ticker(ticker)
        price_history = data.history(period="1y")
        breakpoint()
        x_p = price_history.index
        y_p = price_history.Close
        plt.plot(x_p, y_p)
    plt.show()


#dividend_plot(["AAPL", "MSFT"])
price_plot(["AAPL", "MSFT"])