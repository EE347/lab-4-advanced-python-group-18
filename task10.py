import csv
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd

data = pd.read_csv('/home/pi/ee347/lab-4-advanced-python-group-18/task9.csv')

data['Date'] = pd.to_datetime(data['Date'], format='%d/%m/%Y')

data.set_index('Date', inplace=True)

plt.figure(figsize=(8,6))
for column in data.columns:
    start_value = data[column].iloc[0]
    end_value = data[column].iloc[-1]
    percentage_change = ((end_value - start_value) / start_value) * 100
    plt.plot(data.index, data[column], label=f"{column} (+{percentage_change:.2f}%)")

plt.xlabel('Date')
plt.ylabel('Stock Prices')
plt.title('Stock prices over time')
plt.legend()
plt.grid(True)
plt.show()


