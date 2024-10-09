import csv
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as ply

data=pd.read_csv('/home/pi/ee347/lab-4-advanced-python-group-18/task9.csv')

data['Date']= pd.to_datetime(data['Date'], format='%d/%m/%Y')

data.set_index('Date', inplace=True)

plt.figure(figsize=(8,6))
for column in data.columns:
    plt.plot(data.index, data[column], label=column)

plt.xlabel('Date')
plt.ylabel('Stock Prices')
plt.title('Stock prices over time')
plt.legend()
plt.grid(True)
plt.show()



