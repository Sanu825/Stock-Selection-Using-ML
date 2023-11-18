import yfinance as yf
import pandas as pd
import datetime
from pathlib import Path    # Import the pathlib library

# Replace 'Stock_symbol' with the stock symbol you are interested in
symbol = 'UPL.NS'

# Specify the directory path where you want to save the file
download_directory = Path("D:\Programming\Stock Selections\Stock-Selection-Using-ML\Collect_Stock_Historical_Data\Banking_Sector")  # Replace with your desired directory

# Calculate the end date as today
end_date = pd.to_datetime('today').strftime('%Y-%m-%d')

# Calculate the start date as 5 years nearest full calender year
start_date = (pd.to_datetime('today') - pd.DateOffset(years=4)).replace(month=1, day=1).strftime('%Y-%m-%d')

# Download historical data from Yahoo Finance for the last 5 years
stock_data = yf.download(symbol, start=start_date, end=end_date)

# Save the data to a CSV file in the specified directory
csv_file_path = download_directory / f'{symbol}_historical_data.csv'
stock_data.to_csv(csv_file_path)


