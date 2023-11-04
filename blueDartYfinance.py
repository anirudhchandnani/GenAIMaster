# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 15:57:41 2023

@author: anirudh
"""

import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta


yest_data = pd.read_csv(r"C:\Users\LENOVO\Desktop\work\github\blue_dart_stock_data.csv")
yest_data['Datetime'] = pd.to_datetime(yest_data['Datetime'],utc = True)

# Define the stock symbol (Blue Dart Express)
symbol = "BLUEDART.BO"

# Calculate the date range (previous 7 days)
end_date = datetime.now()
start_date = end_date - timedelta(days=7)

# Download stock data from Yahoo Finance
stock_data = yf.download(tickers="GC=F", period="5d", interval="1m", start = start_date, end = end_date ).reset_index()

# Save the data to a CSV file

stock_data['Datetime'] = pd.to_datetime(stock_data['Datetime'], utc = True)
stock_data = yest_data.append(stock_data).reset_index(drop = True)
stock_data['Datetime'] = stock_data['Datetime'].dt.strftime('%Y-%m-%d %H:%M:%S')


stock_data =  stock_data.drop_duplicates(subset = ['Datetime'])

stock_data.to_csv(r"C:\Users\LENOVO\Desktop\work\github\blue_dart_stock_data.csv", index = None)







# Updated date: (2023-11-04)