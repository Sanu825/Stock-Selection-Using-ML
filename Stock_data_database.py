import getpass  # Import the getpass module for secure password input
import yfinance as yf
import pandas as pd
from pathlib import Path    # Import the pathlib library
from sqlalchemy import create_engine, Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker
from requests.exceptions import HTTPError

# Replace stock_symbols with the list of stock symbols you are interested in
stock_symbols = ['AAPL', 'GOOGL', 'MSFT', 'AMZN']

# Specify the directory path where you want to save the files
download_directory = Path("D:/Programming/Stock Selections/Stock-Selection-Using-ML/Collect_Stock_Data/US_Stock")

# Calculate the end date as today
end_date = pd.to_datetime('today').strftime('%Y-%m-%d')

# Calculate the start date as 5 years nearest full calendar year
start_date = (pd.to_datetime('today') - pd.DateOffset(years=5)).replace(month=1, day=1).strftime('%Y-%m-%d')

# Set up the PostgreSQL database connection
# Prompt the user for PostgreSQL username and password
db_user = input("Enter your PostgreSQL username: ")
db_password = getpass.getpass("Enter your PostgreSQL password: ")

db_host = "localhost"
db_port = "5432"
db_name = "your_postgres_database"

# Create a PostgreSQL engine
engine = create_engine(f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}")

# Define the database schema using SQLAlchemy
Base = declarative_base()

class Company(Base):
    __tablename__ = "stock_info"
    symbol = Column(String, primary_key=True)
    name = Column(String)
    sector = Column(String)

class StockPrice(Base):
    __tablename__ = "stock_price"
    id = Column(Integer, primary_key=True)
    symbol = Column(String, ForeignKey("stock_info.symbol"))
    date = Column(Date)
    open_price = Column(Float)
    high_price = Column(Float)
    low_price = Column(Float)
    close_price = Column(Float)
    volume = Column(Integer)

# Create tables in the database
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

try:
    # Loop through each stock symbol
    for symbol in stock_symbols:
        try:
            # Download historical data from Yahoo Finance for the last 5 years
            stock_data = yf.download(symbol, start=start_date, end=end_date)

            # Save the data to a CSV file in the specified directory
            csv_file_path = download_directory / f'{symbol}_historical_data.csv'
            stock_data.to_csv(csv_file_path)

            # Insert stock information into the database
            stock_info = yf.Ticker(symbol).info
            company = Company(symbol=symbol, name=stock_info.get('longName'), sector=stock_info.get('sector'))
            session.merge(company)

            # Insert historical prices into the database
            for index, row in stock_data.iterrows():
                stock_price = StockPrice(symbol=symbol, date=index, open_price=row['Open'], high_price=row['High'], low_price=row['Low'], close_price=row['Close'], volume=row['Volume'])
                session.merge(stock_price)

        except HTTPError as e:
            print(f"Error processing {symbol}: {e}")
            continue  # Continue to the next stock symbol if an HTTPError occurs

        except Exception as e:
            print(f"Unexpected error processing {symbol}: {e}")
            continue  # Continue to the next stock symbol for any other unexpected errors

    # Commit changes to the database
    session.commit()

except Exception as e:
    print(f"Error: {e}")
    session.rollback()

finally:
    session.close()
