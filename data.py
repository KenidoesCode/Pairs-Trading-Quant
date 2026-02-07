import yfinance as yf
import pandas as pd

def get_data(ticker, start="2020-01-01"):
    data = yf.download(ticker, start=start, auto_adjust=False)

    # If columns are multi-level, flatten them
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)

    return data["Adj Close"]
