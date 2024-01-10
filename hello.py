# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 01:34:58 2023

@author: anirudh
"""



import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import os
import subprocess
from datetime import date

repo_url = "https://github.com/anirudhchandnani/GenAIMaster.git"

import time

# Sleep for two seconds
time.sleep(2)

# Set the path to your local clone of the repository
local_repo_path = r"C:\Users\LENOVO\Desktop\work\github"

# Change to the local repository directory
os.chdir(local_repo_path)
file_to_modify = "blueDartYfinance.py"  # Change this to the actual file you want to modify
with open(file_to_modify, "a") as file:
    file.write(f"\n# Updated date: ({date.today()})")


yest_data = pd.read_csv(r"C:\Users\LENOVO\Desktop\work\github\blue_dart_stock_data.csv")
yest_data['Datetime'] = pd.to_datetime(yest_data['Datetime'],utc = True)
###########+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# Define the stock symbol (Blue Dart Express)
symbol = "BLUEDART.BO"

# Calculate the date range (previous 7 days)
end_date = datetime.now()
start_date = end_date - timedelta(days=5)

###########+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# Download stock data from Yahoo Finance
stock_data = yf.download(tickers="GC=F", interval="1m", start = start_date, end = end_date ).reset_index()
###########+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

stock_data['Datetime'] = pd.to_datetime(stock_data['Datetime'], utc = True)
#####################ERROR HERE had to use _append instead of append
stock_data = yest_data._append(stock_data).reset_index(drop = True)
stock_data['Datetime'] = stock_data['Datetime'].dt.strftime('%Y-%m-%d %H:%M:%S')


stock_data =  stock_data.drop_duplicates(subset = ['Datetime'])

stock_data.to_csv(r"C:\Users\LENOVO\Desktop\work\github\blue_dart_stock_data.csv", index = None)

print('hello'+str(stock_data.shape[0]))
import time
time.sleep(2)


# Random change: 2 (2023-11-04)
# Random change: 79 (2023-11-04)
# Random change: 26 (2023-11-04)
# Random change: 3 (2023-11-04)
# Random change: 84 (2023-11-04)
# Random change: 89 (2023-11-04)
# Random change: 83 (2023-11-04)
# Random change: 43 (2023-11-04)
# Random change: 99 (2023-11-04)
# Random change: 51 (2023-11-04)
# Random change: 6 (2023-11-04)
# Random change: 92 (2023-11-04)
# Random change: 29 (2023-11-04)
# Random change: 64 (2023-11-04)
# Random change: 2 (2023-11-04)
# Random change: 62 (2023-11-04)
# Random change: 46 (2023-11-04)
# Random change: 70 (2023-11-04)
# Random change: 94 (2023-11-04)
# Random change: 7 (2023-11-04)
# Random change: 30 (2023-11-04)
# Random change: 4 (2023-11-04)
# Random change: 93 (2023-11-04)
# Random change: 51 (2023-11-04)
# Random change: 6 (2023-11-04)
# Random change: 49 (2023-11-04)
# Random change: 71 (2023-11-06)
# Random change: 10 (2023-11-06)
# Random change: 81 (2023-11-06)
# Random change: 75 (2023-11-06)
# Random change: 32 (2023-11-06)
# Random change: 40 (2023-11-06)
# Random change: 79 (2023-11-06)
# Random change: 59 (2023-11-06)
# Random change: 62 (2023-11-06)
# Random change: 33 (2023-11-06)
# Random change: 34 (2023-11-08)
# Random change: 30 (2023-11-08)
# Random change: 95 (2023-11-08)
# Random change: 18 (2023-11-08)
# Random change: 37 (2023-11-08)
# Random change: 61 (2023-11-08)
# Random change: 81 (2023-11-11)
# Random change: 48 (2023-11-18)
# Random change: 4 (2023-11-19)
# Random change: 75 (2023-11-19)
# Random change: 21 (2023-11-19)
# Random change: 73 (2023-11-19)
# Random change: 86 (2023-11-19)
# Random change: 57 (2023-11-26)
# Random change: 80 (2023-11-26)
# Random change: 19 (2023-11-26)
# Random change: 41 (2023-11-26)
# Random change: 98 (2023-12-02)
# Random change: 44 (2023-12-02)
# Random change: 9 (2023-12-03)
# Random change: 57 (2023-12-03)
# Random change: 97 (2023-12-03)
# Random change: 33 (2023-12-20)
# Random change: 96 (2023-12-20)
# Random change: 89 (2023-12-20)
# Random change: 54 (2023-12-20)
# Random change: 53 (2023-12-26)
# Random change: 91 (2023-12-26)
# Random change: 59 (2023-12-26)
# Random change: 86 (2023-12-26)
# Random change: 72 (2023-12-27)
# Random change: 3 (2023-12-27)
# Random change: 8 (2023-12-27)
# Random change: 58 (2023-12-28)
# Random change: 59 (2023-12-28)
# Random change: 10 (2023-12-28)
# Random change: 45 (2024-01-02)
# Random change: 26 (2024-01-03)
# Random change: 47 (2024-01-03)
# Random change: 11 (2024-01-03)
# Random change: 24 (2024-01-03)
# Random change: 48 (2024-01-03)
# Random change: 28 (2024-01-03)
# Random change: 6 (2024-01-04)
# Random change: 65 (2024-01-04)
# Random change: 65 (2024-01-04)
# Random change: 21 (2024-01-04)
# Random change: 23 (2024-01-04)
# Random change: 88 (2024-01-04)
# Random change: 1 (2024-01-06)
# Random change: 94 (2024-01-07)
# Random change: 1 (2024-01-07)
# Random change: 87 (2024-01-07)
# Random change: 94 (2024-01-07)
# Random change: 70 (2024-01-07)
# Random change: 33 (2024-01-07)
# Random change: 79 (2024-01-07)
# Random change: 10 (2024-01-08)
# Random change: 44 (2024-01-08)
# Random change: 49 (2024-01-08)
# Random change: 72 (2024-01-08)
# Random change: 16 (2024-01-08)
# Random change: 6 (2024-01-08)
# Random change: 14 (2024-01-10)
# Random change: 94 (2024-01-10)
# Random change: 70 (2024-01-10)
# Random change: 95 (2024-01-10)