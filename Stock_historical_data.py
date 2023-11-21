import yfinance as yf
import pandas as pd
import datetime
from pathlib import Path    # Import the pathlib library

# Replace 'Stock_symbol' with the stock symbol you are interested in
# symbol = ['BAJFINANCE.NS']

# Private Bank stock symbol
symbols = ['AUBANK.NS', 'AXISBANK.NS', 'BANDHANBNK.NS', 'CSBBANK.NS', 'CUB.NS', 'DCBBANK.NS', 'DHANBANK.NS', 'EQUITASBNK.NS', 'ESAFSFB.NS', 'FEDERALBNK.NS', 'FINOPB.NS', 'HDFCBANK.NS', 'ICICIBANK.NS', 'IDBI.NS', 'IDFCFIRSTB.NS', 'INDUSINDBK.NS', 'J&KBANK.NS', 'KARURVYSYA.NS', 'KOTAKBANK.NS', 'KTKBANK.NS', 'RBLBANK.NS', 'SOUTHBANK.NS', 'SURYODAY.NS', 'TMB.NS', 'UJJIVANSFB.NS', 'UTKARSHBNK.NS', 'YESBANK.NS' ]

# Public Bank stock symbol
# symbols = ['BANKBARODA.NS', 'BANKINDIA.NS', 'CANBK.NS', 'CENTRALBK.NS', 'INDIANB.NS', 'IOB.NS', 'MAHABANK.NS', 'PNB.NS', 'PSB.NS', 'SBIN.NS', 'UCOBANK.NS', 'UNIONBANK.NS']

# IT_Sector stock symbol
# symbols = ['AFFLE.NS', 'BSOFT.NS', 'CAMS.NS', 'CMSINFO.NS', 'COFORGE.NS', 'CYIENT.NS', 'ECLERX.NS', 'FSL.NS', 'HAPPSTMNDS.NS', 'HCLTECH.NS', 'INFY.NS', 'INTELLECT.NS', 'KPITTECH.NS', 'LTIM.NS', 'LTTS.NS', 
#            'MASTEK.NS', 'MPHASIS.NS', 'NAUKRI.NS', 'NEWGEN.NS', 'OFSS.NS', 'PERSISTENT.NS', 'RATEGAIN.NS', 'ROUTE.NS', 'SONATSOFTW.NS', 'TANLA.NS', 'TATAELXSI.NS', 'TCS.NS', 'TECHM.NS', 'TEJASNET.NS', 'WIPRO.NS', 
#            'ZENSARTECH.NS', 'ZENTEC.NS']

# Top_50 stock symbol
# symbols = ['ADANIENT.NS', 'ADANIPORTS.NS', 'APOLLOHOSP.NS', 'ASIANPAINT.NS', 'AXISBANK.NS', 'BAJAJ-AUTO.NS', 'BAJAJFINSV.NS', 'BAJAJFINANCE.NS', 'BHARTIARTL.NS', 'BPCL.NS', 'BRITANNIA.NS', 'CIPLA.NS', 
#            'COALINDIA.NS', 'DIVISLAB.NS', 'DRREDDY.NS', 'EICHERMOT.NS', 'GRASIM.NS', 'HCLTECH.NS', 'HDFCBANK.NS', 'HDFCLIFE.NS', 'HEROMOTOCO.NS', 'HINDALCO.NS', 'HINDUNILVR.NS', 'ICICIBANK.NS', 'INDUSINDBK.NS', 
#            'INFY.NS', 'ITC.NS', 'JIOFIN.NS', 'JSWSTEEL.NS', 'KOTAKBANK.NS', 'LT.NS', 'LTIM.NS', 'M&M.NS', 'MARUTI.NS', 'NESTLEIND.NS', 'NTPC.NS', 'ONGC.NS', 'POWERGRID.NS', 'RELIANCE.NS', 'SBILIFE.NS', 'SBIN.NS', 
#            'SUNPHARMA.NS', 'TATACONSUM.NS', 'TATAMOTORS.NS', 'TATASTEEL.NS', 'TCS.NS', 'TECHM.NS', 'TITAN.NS', 'ULTRACEMCO.NS', 'UPL.NS', 'WIPRO.NS'] 

# US_Stock Symbol
# symbols = ['UNH', 'MSFT', 'GS', 'HD', 'MCD', 'AMZN', 'CAT', 'V', 'CRM', 'BA', 'HON', 'AAPL', 'TRV', 'AXP', 'WMT', 'IBM', 'JPM', 'PG', 'JNJ', 'CVX', 'NKE', 'MRK', 'DIS', 'MMM', 'KO', 'DOW', 'CSCO', 'INTC', 'VZ', 'WBA']

# Specify the directory path where you want to save the file
download_directory = Path("D:\Programming\Stock Selections\Stock-Selection-Using-ML\Collect_Stock_Historical_Data\Banking_Sector\Private_Bank")  # Replace with your desired directory

# Calculate the end date as today
end_date = pd.to_datetime('today').strftime('%Y-%m-%d')

# Calculate the start date as 5 years nearest full calender year
start_date = (pd.to_datetime('today') - pd.DateOffset(years=4)).replace(month=1, day=1).strftime('%Y-%m-%d')




# Download historical data from Yahoo Finance for the last 5 years
for symbol in symbols:
    stock_data = yf.download(symbol, start=start_date, end=end_date)

    # Save the data to a CSV file in the specified directory
    csv_file_path = download_directory / f'{symbol}_historical_data.csv'
    stock_data.to_csv(csv_file_path)


