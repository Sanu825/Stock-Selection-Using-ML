from alpha_vantage.timeseries import TimeSeries
import pandas as pd
import datetime
import time     # Import the time module for rate limiting

# Replace 'api_key' with your actual Alpha Vantage API key
api_key = '9XW0SN1H49A7N4KH'
symbol = 'TCS'

# Create an instance of the TimeSeries class with your API key
ts = TimeSeries(key=api_key, output_format='pandas')

# Calculate the start and end dates for the last 5 years
end_date = datetime.datetime.today().strftime('%Y-%m-%d')
start_date = (datetime.datetime.today() - datetime.timedelta(days=5 * 365)).strftime('%Y-%m-%d')

# Define a function to handle rate limiting
def get_alpha_vantage_data():
    retries = 5
    for _ in range(retries):
        try:
            # Get historical daily data
            data, meta_data = ts.get_daily(symbol=symbol, outputsize='full')

            # Filter data for the specified time range
            filtered_data = data.loc[start_date:end_date]

            # Print the data
            print(filtered_data)

            # Save the data to a CSV file
            filtered_data.to_csv(f'{symbol}_historical_data.csv')

            break  # Exit the loop if successful
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(15)  # Wait for 15 seconds before retrying

# Call the function to get data
get_alpha_vantage_data()