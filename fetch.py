import yfinance as yf
import pandas as pd

# Define the stock tickers and date range
tickers = ["AAPL", "MSFT", "AMZN", "NVDA", "META"]
start_date = "2018-12-31"
end_date = "2023-12-31"

# Loop through each ticker, download the data, and save to a CSV file
for ticker in tickers:
    # Download monthly data
    data = yf.download(ticker, start=start_date, end=end_date, interval="1mo")
    
    # Save data to CSV
    csv_filename = f"{ticker}_monthly_data.csv"
    data.to_csv(csv_filename)
    print(f"Saved data for {ticker} to {csv_filename}")
