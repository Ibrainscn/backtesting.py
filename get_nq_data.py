import yfinance as yf
import datetime
import pandas as pd

tickerSymbol = "NQ=F"
start_date = datetime.datetime(2023, 3, 9)
end_date = datetime.datetime(2023, 3, 16)

tickerData = yf.download(tickerSymbol, interval='1m', start=start_date, end=end_date)
tickerData.to_csv("NQ.csv")
print("NQ tickerData:")
print(tickerData)
