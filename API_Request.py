
import requests

# Replace 'api_key' with your actual Alpha Vantage API key
api_key = '9XW0SN1H49A7N4KH'
symbol = ''  # Replace with the symbol of the stock you want to query

# Alpha Vantage API endpoint for time series data
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=1min&apikey={api_key}'

# Make the API request
response = requests.get(url)

# Check the response status code
if response.status_code == 200:
    print("API key is working properly.")
else:
    print(f"API key may not be valid. Status code: {response.status_code}")
    print(response.text)  # Print the response content for more details
