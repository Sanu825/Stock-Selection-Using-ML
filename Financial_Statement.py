import requests

# Replace 'YOUR_API_KEY' with your actual Alpha Vantage API key
api_key = '9XW0SN1H49A7N4KH'

# Replace 'AAPL' with the stock symbol you are interested in
symbol = 'HDFCBANK.NS'

# Alpha Vantage API endpoint URLs
balance_sheet_url = f'https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol={symbol}&apikey={api_key}'
cash_flow_url = f'https://www.alphavantage.co/query?function=CASH_FLOW&symbol={symbol}&apikey={api_key}'
income_statement_url = f'https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol={symbol}&apikey={api_key}'

# Function to make API request and return data
def get_alpha_vantage_data(url):
    response = requests.get(url)
    data = response.json()
    return data

# Get balance sheet data
balance_sheet_data = get_alpha_vantage_data(balance_sheet_url)
print("Balance Sheet Data:")
print(balance_sheet_data)

# Get cash flow data
cash_flow_data = get_alpha_vantage_data(cash_flow_url)
print("\nCash Flow Data:")
print(cash_flow_data)

# Get income statement data
income_statement_data = get_alpha_vantage_data(income_statement_url)
print("\nIncome Statement Data:")
print(income_statement_data)
