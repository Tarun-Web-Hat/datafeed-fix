import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Example function to fetch stock data (replace with actual data fetching logic)
def fetch_stock_data(ticker):
    # Replace with real data fetching logic
    dates = pd.date_range('2023-01-01', '2023-12-31')
    prices = np.random.random(len(dates)) * 100
    return pd.DataFrame({'Date': dates, 'Price': prices}).set_index('Date')

# Fetch data for two stocks
stock1 = fetch_stock_data('STOCK1')
stock2 = fetch_stock_data('STOCK2')

# Calculate correlation
correlation = stock1['Price'].corr(stock2['Price'])
print(f'Correlation between STOCK1 and STOCK2: {correlation}')

# Plot data
plt.figure(figsize=(14, 7))
plt.plot(stock1.index, stock1['Price'], label='STOCK1')
plt.plot(stock2.index, stock2['Price'], label='STOCK2')
plt.title('Stock Prices')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()

