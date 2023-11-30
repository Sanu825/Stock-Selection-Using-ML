import pandas as pd
from datetime import datetime, timedelta

# Calculate the start date (current date - 6 years)
# end_date = datetime.now()
# start_date = (end_date - timedelta(days=6*365)).replace(day=1)

# Load data from a local CSV file
# Assuming the CSV file has columns like 'Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', and 'Volume'
# You may need to adjust the columns based on the structure of your CSV file
symbol  = 'AAPL'
dfSPY = pd.read_csv(f"{symbol}.csv")

# Filter rows where High is not equal to Low
dfSPY = dfSPY[dfSPY['High'] != dfSPY['Low']]

# Reset index
dfSPY.reset_index(inplace=True, drop=True)

dfSPY.head()
