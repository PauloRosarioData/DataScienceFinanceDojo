import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns sns.set_style('white')

"""This script shows how to load and plot
a few columns from the time series data CSV file.
"""

# load data
raw_data = pd.read_csv('coding_dojo_data.csv')
raw_data.index  = pd.to_datetime(raw_data['timestamp'].values)
raw_data.drop('Unnamed: 0', axis=1, inplace=True)

# plot a few columns
raw_data[['column_0', 'column_1']].plot(alpha=0.8, figsize=(10, 6), title='Time Series Plot')
plt.grid()
plt.xlabel('Date')
plt.ylabel('Value')
plt.show()
