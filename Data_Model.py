import os
import pandas as pd
import pandas_ta as ta
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


def load_stock_data(directory, symbol):
    file_path = os.path.join(directory, symbol)
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    else:
        print(f"Data not found for {symbol}")
        return None

def calculate_technical_indicators(data):
    # Calculate moving averages
    data['MA21'] = ta.sma(data['close'], 21)
    data['MA50'] = ta.sma(data['close'], 50)
    data['MA100'] = ta.sma(data['close'], 100)
    data['MA200'] = ta.sma(data['close'], 200)

    # Add other technical indicators
    # Example: RSI (Relative Strength Index)
    data['RSI'] = ta.rsi(data['close'], 44)

    # Add more indicators as needed

def train_ml_model(data, algorithm='RandomForest'):
    features = ['MA21', 'MA50', 'MA100', 'MA200', 'RSI']
    X = data[features]
    y = data['buy']  # Assuming 'buy' is the target variable indicating buy/sell/hold

    # Split the data into training (80%) and testing (20%)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    if algorithm == 'RandomForest':
        model = RandomForestClassifier()
    # Add other algorithms as needed

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)

    return model, accuracy

# Example usage for backtesting on a particular stock (e.g., AAPL)
symbol = "AAPL"
directory = 'D:\Programming\Stock Selections\Stock-Selection-Using-ML\Processing_Historical_Data\Dow_Jones' + '\\' + symbol +'.csv'

stock_data = load_stock_data(symbol)

if stock_data is not None:
    calculate_technical_indicators(stock_data)

    # Train model using RandomForest as default, change 'algorithm' parameter to use a different one
    trained_model, accuracy = train_ml_model(stock_data, algorithm='RandomForest')
    print(f"Accuracy using RandomForest: {accuracy}")

    # # Backtest the model on the entire historical data
    # backtest_X = stock_data[features]
    # backtest_y = stock_data['buy']

    # backtest_predictions = trained_model.predict(backtest_X)
    # backtest_accuracy = accuracy_score(backtest_y, backtest_predictions)
    # print(f"Backtesting Accuracy: {backtest_accuracy}")
