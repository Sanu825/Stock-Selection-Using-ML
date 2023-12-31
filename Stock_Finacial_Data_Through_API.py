import requests
import json
import pandas
from pathlib import Path
from datetime import datetime, timedelta

# Replace 'YOUR_API_KEY' with your actual Alpha Vantage API key
api_key = '9XW0SN1H49A7N4KH'

# Replace 'AAPL' with the stock symbol you are interested in
symbols = ['UNH', 'MSFT', 'GS', 'HD', 'MCD', 'AMZN', 'CAT', 'V', 'CRM', 'BA', 'HON', 'AAPL', 'TRV', 'AXP', 'WMT', 'IBM', 'JPM', 'PG', 'JNJ', 'CVX', 'NKE']
# symbols = ['MRK', 'DIS', 'MMM', 'KO', 'DOW', 'CSCO', 'INTC', 'VZ', 'WBA']

# Specify the parent directory path where you want to save the files
parent_directory = Path("D:/Programming/Stock Selections/Stock-Selection-Using-ML/Collect_Stock_Financial_Data/US_Stock")



# Create a directory for the specific stock if it doesn't exist
for symbol in symbols:
    stock_directory = parent_directory / symbol
    stock_directory.mkdir(parents=True, exist_ok=True)

    # Function to make API request and save data to a JSON file
    def save_alpha_vantage_data(url, file_path):
        response = requests.get(url)
        data = response.json()
        with open(file_path, 'w') as file:
            json.dump(data, file)
        print(f"Data saved to {file_path}")


    # Calculate the end date as today
    end_date = datetime.now().strftime('%Y-%m-%d')

    # Calculate the start date as 6 years ago, rounded to the beginning of the quarter
    start_date = (datetime.now() - timedelta(days=5*365.25)).replace(month=datetime.now().month - (datetime.now().month - 1) % 3, day=1).strftime('%Y-%m-%d')

    # Create a dictionary to store all financial data and metrics
    financial_data = {}

    # Download balance sheet, income statement, and cash flow data
    balance_sheet_url = f'https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol={symbol}&apikey={api_key}&interval=quarterly'
    income_statement_url = f'https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol={symbol}&apikey={api_key}&interval=quarterly'
    cash_flow_url = f'https://www.alphavantage.co/query?function=CASH_FLOW&symbol={symbol}&apikey={api_key}&interval=quarterly'
    overview_url = f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={symbol}&apikey={api_key}'


    # # Create a directory for the specific stock if it doesn't exist
    # stock_directory = parent_directory / symbol
    # stock_directory.mkdir(parents=True, exist_ok=True)

    # Download balance sheet data
    balance_sheet_file_path = stock_directory / f'{symbol}_balance_sheet.json'
    save_alpha_vantage_data(balance_sheet_url, balance_sheet_file_path)
    with open(balance_sheet_file_path, 'r') as file:
        financial_data['balance_sheet'] = json.load(file)

    # Download income statement data
    income_statement_file_path = stock_directory / f'{symbol}_income_statement.json'
    save_alpha_vantage_data(income_statement_url, income_statement_file_path)
    with open(income_statement_file_path, 'r') as file:
        financial_data['income_statement'] = json.load(file)

    # Download cash flow data
    cash_flow_file_path = stock_directory / f'{symbol}_cash_flow.json'
    save_alpha_vantage_data(cash_flow_url, cash_flow_file_path)
    with open(cash_flow_file_path, 'r') as file:
        financial_data['cash_flow'] = json.load(file)

    # Download additional financial metrics
    overview_file_path = stock_directory / f'{symbol}_overview.json'
    save_alpha_vantage_data(overview_url, overview_file_path)
    with open(overview_file_path, 'r') as file:
        financial_data['overview'] = json.load(file)

