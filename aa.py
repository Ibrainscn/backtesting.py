import pandas as pd
import mplfinance as mpf

# Create sample data
data = pd.DataFrame({
    'Date': pd.date_range(start='2022-02-26', end='2022-03-18'),
    'Open': [100, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200, 195],
    'High': [110, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200, 205, 210, 200],
    'Low':  [90, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 180],
    'Close': [110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200, 195, 190],
    'Volume': [1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500, 10000, 10500, 11000]
})

# Convert index to DatetimeIndex
data.index = pd.to_datetime(data.index)

# Create the chart
mpf.plot(data, type='candle', volume=True, mav=(10, 20), figratio=(12,6), figscale=0.85, title='My Chart', ylabel='Price ($)', ylabel_lower='Volume')
