import yfinance as yf
import pandas as pd
import datetime
from pathlib import Path    # Import the pathlib library

# Replace 'Stock_symbol' with the stock symbol you are interested in
# Private Bank stock symbol
# symbol = 'SURYODAY.NS'
# symbol = ['AUBANK.NS', 'AXISBANK.NS', 'BANDHANBNK.NS', 'CSBBANK.NS', 'CUB.NS', 'DCBBANK.NS', 'DHANBANK.NS', 'EQUITASBNK.NS', 'ESAFSFB.NS', 'FEDERALBNK.NS', 'FINOPB.NS', 'HDFCBANK.NS', 'ICICIBANK.NS', 'IDBI.NS', 'IDFCFIRSTB.NS', 'INDUSINDBK.NS', 'J&KBANK.NS', 'KARURVYSYA.NS', 'KOTAKBANK.NS', 'KTKBANK.NS', 'RBLBANK.NS', 'SOUTHBANK.NS', 'SURYODAY.NS', 'TMB.NS', 'UJJIVANSFB.NS', 'UTKARSHBNK.NS', 'YESBANK.NS' ]

# Public Bank stock symbol
symbol = ['BANKBARODA.NS', 'BANKINDIA.NS', 'CANBK.NS', 'CENTRALBK.NS', 'INDIANB.NS', 'IOB.NS', 'MAHABANK.NS', 'PNB.NS', 'PSB.NS', 'SBIN.NS', 'UCOBANK.NS, UNIONBANK.NS']

# Specify the directory path where you want to save the file
download_directory = Path("D:\Programming\Stock Selections\Stock-Selection-Using-ML\Collect_Stock_Historical_Data\Banking_Sector\Public_Bank")  # Replace with your desired directory

# Calculate the end date as today
end_date = pd.to_datetime('today').strftime('%Y-%m-%d')

# Calculate the start date as 5 years nearest full calender year
start_date = (pd.to_datetime('today') - pd.DateOffset(years=4)).replace(month=1, day=1).strftime('%Y-%m-%d')

# Download historical data from Yahoo Finance for the last 5 years
for symbol in symbol:
    stock_data = yf.download(symbol, start=start_date, end=end_date)

    # Save the data to a CSV file in the specified directory
    csv_file_path = download_directory / f'{symbol}_historical_data.csv'
    stock_data.to_csv(csv_file_path)


