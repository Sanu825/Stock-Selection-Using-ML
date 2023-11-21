import yfinance as yf
import pandas as pd
from pathlib import Path
from datetime import datetime, timedelta

# Replace 'ticker' with the stock symbol you are interested in
tickers = ['AUBANK.NS', 'AXISBANK.NS', 'BANDHANBNK.NS', 'CSBBANK.NS', 'CUB.NS', 'DCBBANK.NS', 'DHANBANK.NS', 'EQUITASBNK.NS', 'ESAFSFB.NS', 'FEDERALBNK.NS', 'FINOPB.NS', 'HDFCBANK.NS', 
           'ICICIBANK.NS', 'IDBI.NS', 'IDFCFIRSTB.NS', 'INDUSINDBK.NS', 'J&KBANK.NS', 'KARURVYSYA.NS', 'KOTAKBANK.NS', 'KTKBANK.NS', 'RBLBANK.NS', 'SOUTHBANK.NS', 'SURYODAY.NS', 'TMB.NS', 
           'UJJIVANSFB.NS', 'UTKARSHBNK.NS', 'YESBANK.NS' ]
# tickers = ['BANKBARODA.NS', 'BANKINDIA.NS', 'CANBK.NS', 'CENTRALBK.NS', 'INDIANB.NS', 'IOB.NS', 'MAHABANK.NS', 'PNB.NS', 'PSB.NS', 'SBIN.NS', 'UCOBANK.NS', 'UNIONBANK.NS']

# IT_Sector stock
tickers = ['AFFLE.NS', 'BSOFT.NS', 'CAMS.NS', 'CMSINFO.NS', 'COFORGE.NS', 'CYIENT.NS', 'ECLERX.NS', 'FSL.NS', 'HAPPSTMNDS.NS', 'HCLTECH.NS', 'INFY.NS', 'INTELLECT.NS', 
           'KPITTECH.NS', 'LTIM.NS', 'LTTS.NS', 'MASTEK.NS', 'MPHASIS.NS', 'NAUKRI.NS', 'NEWGEN.NS', 'OFSS.NS', 'PERSISTENT.NS', 'RATEGAIN.NS', 'ROUTE.NS', 'SONATSOFTW.NS', 
           'TANLA.NS', 'TATAELXSI.NS', 'TCS.NS', 'TECHM.NS', 'TEJASNET.NS', 'WIPRO.NS', 'ZENSARTECH.NS', 'ZENTEC.NS']

# Top_50 stock
tickers = ['ADANIENT.NS', 'ADANIPORTS.NS', 'APOLLOHOSP.NS', 'ASIANPAINT.NS', 'AXISBANK.NS', 'BAJAJ-AUTO.NS', 'BAJAJFINSV.NS', 'BAJAJFINANCE.NS', 'BHARTIARTL.NS', 'BPCL.NS', 
           'BRITANNIA.NS', 'CIPLA.NS', 'COALINDIA.NS', 'DIVISLAB.NS', 'DRREDDY.NS', 'EICHERMOT.NS', 'GRASIM.NS', 'HCLTECH.NS', 'HDFCBANK.NS', 'HDFCLIFE.NS', 'HEROMOTOCO.NS', 
           'HINDALCO.NS', 'HINDUNILVR.NS', 'ICICIBANK.NS', 'INDUSINDBK.NS', 'INFY.NS', 'ITC.NS', 'JIOFIN.NS', 'JSWSTEEL.NS', 'KOTAKBANK.NS', 'LT.NS', 'LTIM.NS', 'M&M.NS', 'MARUTI.NS', 
           'NESTLEIND.NS', 'NTPC.NS', 'ONGC.NS', 'POWERGRID.NS', 'RELIANCE.NS', 'SBILIFE.NS', 'SBIN.NS', 'SUNPHARMA.NS', 'TATACONSUM.NS', 'TATAMOTORS.NS', 'TATASTEEL.NS', 'TCS.NS', 'TECHM.NS', 
           'TITAN.NS', 'ULTRACEMCO.NS', 'UPL.NS', 'WIPRO.NS']

# Specify the base folder where stock folders will be created
file_path = Path('D:/Programming/Stock Selections/Stock-Selection-Using-ML/Collect_Stock_Financial_Data')

# Iterate over each stock
for ticker in tickers:
    # Create a folder for the stock if it doesn't exist
    stock_folder = file_path / ticker
    stock_folder.mkdir(parents=True, exist_ok=True)

    # Print the stock symbol before saving each file
    print(f"Downloading data for stock: {ticker}")

    # Get the balance sheet for the stock
    balance_sheet = yf.Ticker(ticker).balance_sheet

    # Save balance sheet data in a CSV file
    balance_sheet_csv_path = stock_folder / f'{ticker}_balance_sheet.csv'
    balance_sheet.to_csv(balance_sheet_csv_path)
    

    # Get the cash flow statement for the stock
    cash_flow = yf.Ticker(ticker).cashflow

    # Save cash flow data in a CSV file
    cash_flow_csv_path = stock_folder / f'{ticker}_cash_flow.csv'
    cash_flow.to_csv(cash_flow_csv_path)
    

    # Get the profit & loss statement for the stock
    profit_loss = yf.Ticker(ticker).financials

    # Save profit & loss data in a CSV file
    profit_loss_csv_path = stock_folder / f'{ticker}_profit_loss.csv'
    profit_loss.to_csv(profit_loss_csv_path)
    

    # Specify the time range for the last 4 years
    end_date = datetime.now().strftime('%Y-%m-%d')
    start_date = (datetime.now() - timedelta(days=5*365)).strftime('%Y-%m-%d')
