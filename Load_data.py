
import pandas as pd

# Replace 'your_file_name.csv' with the actual name of your CSV file
file_name = 'AAPL'

# Construct the full file path by joining the directory path and the file name
file_path = 'D:\Programming\Stock Selections\Stock-Selection-Using-ML\Processing_Historical_Data\Dow_Jones' + '\\' + file_name +'.csv'

# Load the CSV file into a pandas DataFrame
data = pd.read_csv(file_path)

# # Set the display options to show all rows and columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Display the DataFrame
print(data)
