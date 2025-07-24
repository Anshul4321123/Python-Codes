import yfinance as yf
import pandas as pd

# Define parameters
  # Change to any stock symbol
start_date = "2015-01-01"
end_date = "2024-01-01"
output_filename = f"{tic}_data.csv"

# Download data
data = yf.download( start=start_date, end=end_date)

# Save to CSV
data.to_csv(output_filename)

print(f"Data for saved to {output_filename}")
