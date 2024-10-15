import pandas as pd
import yfinance as yf

# List of stock tickers
stocks = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA']

# Fetch stock data
def fetch_stock_data(ticker):
    stock = yf.Ticker(ticker)
    hist = stock.history(period="1d")
    return hist['Close'][0]

# Create a DataFrame to hold the portfolio
portfolio = pd.DataFrame(columns=['Ticker', 'Price'])

# Populate the DataFrame with stock prices
for stock in stocks:
    price = fetch_stock_data(stock)
    new_row = pd.DataFrame({'Ticker': [stock], 'Price': [price]})
    portfolio = pd.concat([portfolio, new_row], ignore_index=True)

print(portfolio)
