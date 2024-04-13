# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 15:57:41 2023

@author: anirudh
"""

# print("hello")

# import yfinance as yf
# import pandas as pd
# from datetime import datetime, timedelta
# import os
# import subprocess
# from datetime import date


# repo_url = "https://github.com/anirudhchandnani/GenAIMaster.git"

# import time

# # Sleep for two seconds
# time.sleep(2)

# # Set the path to your local clone of the repository
# local_repo_path = r"C:\Users\LENOVO\Desktop\work\github"

# # Change to the local repository directory
# os.chdir(local_repo_path)

# # Create a random change in a Python file
# # random_value = random.randint(1, 100)
# file_to_modify = "blueDartYfinance.py"  # Change this to the actual file you want to modify
# with open(file_to_modify, "a") as file:
#     file.write(f"\n# Updated date: ({date.today()})")


# yest_data = pd.read_csv(r"C:\Users\LENOVO\Desktop\work\github\blue_dart_stock_data.csv")
# yest_data['Datetime'] = pd.to_datetime(yest_data['Datetime'],utc = True)

# # Define the stock symbol (Blue Dart Express)
# symbol = "BLUEDART.BO"

# # Calculate the date range (previous 7 days)
# end_date = datetime.now()
# start_date = end_date - timedelta(days=5)

# # Download stock data from Yahoo Finance
# stock_data = yf.download(tickers="GC=F", interval="1m", start = start_date, end = end_date ).reset_index()

# # Save the data to a CSV file

# stock_data['Datetime'] = pd.to_datetime(stock_data['Datetime'], utc = True)
# stock_data = yest_data._append(stock_data).reset_index(drop = True)
# stock_data['Datetime'] = stock_data['Datetime'].dt.strftime('%Y-%m-%d %H:%M:%S')


# stock_data =  stock_data.drop_duplicates(subset = ['Datetime'])

# stock_data.to_csv(r"C:\Users\LENOVO\Desktop\work\github\blue_dart_stock_data.csv", index = None)


# # Commit and push the change
# commit_message = f"Data updated today: ({date.today()})"
# subprocess.run(["git", "add", "."])
# subprocess.run(["git", "commit", "-m", commit_message])
# subprocess.run(["git", "push", "origin", "main"])

# print(f"Data uploaded today  ({date.today()}) {repo_url}")
# time.sleep(2)

########################################################### new code version 2

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

# Fetch changes from the remote repository
subprocess.run(["git", "fetch"])

# Pull changes from the remote repository
subprocess.run(["git", "pull"])

# Create a random change in a Python file
# random_value = random.randint(1, 100)
file_to_modify = "blueDartYfinance.py"  # Change this to the actual file you want to modify
with open(file_to_modify, "a") as file:
    file.write(f"\n# Updated date: ({date.today()})")

yest_data = pd.read_csv(r"C:\Users\LENOVO\Desktop\work\github\blue_dart_stock_data.csv")
yest_data['Datetime'] = pd.to_datetime(yest_data['Datetime'], utc=True)

# Define the stock symbol (Blue Dart Express)
symbol = "BLUEDART.BO"

# Calculate the date range (previous 7 days)
end_date = datetime.now()
start_date = end_date - timedelta(days=5)

# Download stock data from Yahoo Finance
stock_data = yf.download(tickers="GC=F", interval="1m", start=start_date, end=end_date).reset_index()

# Save the data to a CSV file
stock_data['Datetime'] = pd.to_datetime(stock_data['Datetime'], utc=True)
stock_data = yest_data._append(stock_data).reset_index(drop=True)
stock_data['Datetime'] = stock_data['Datetime'].dt.strftime('%Y-%m-%d %H:%M:%S')

stock_data = stock_data.drop_duplicates(subset=['Datetime'])

stock_data.to_csv(r"C:\Users\LENOVO\Desktop\work\github\blue_dart_stock_data.csv", index=None)

# Commit and push the change
commit_message = f"Data updated today: ({date.today()})"
subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit", "-m", commit_message])
subprocess.run(["git", "push", "origin", "main"])

print(f"Data uploaded today  ({date.today()}) {repo_url}")
time.sleep(2)







# Updated date: (2023-11-06)
# Updated date: (2023-11-06)
# Updated date: (2023-11-06)
# Updated date: (2023-11-06)
# Updated date: (2023-11-06)
# Updated date: (2023-11-06)
# Updated date: (2023-11-06)
# Updated date: (2023-11-07)
# Updated date: (2023-11-07)
# Updated date: (2023-11-07)
# Updated date: (2023-11-07)
# Updated date: (2023-11-07)
# Updated date: (2023-11-07)
# Updated date: (2023-11-07)
# Updated date: (2023-11-07)
# Updated date: (2023-11-07)
# Updated date: (2023-11-07)
# Updated date: (2023-11-07)
# Updated date: (2023-11-07)
# Updated date: (2023-11-07)
# Updated date: (2023-11-07)
# Updated date: (2023-11-07)
# Updated date: (2023-11-07)
# Updated date: (2023-11-07)
# Updated date: (2023-11-07)
# Updated date: (2023-11-07)
# Updated date: (2023-11-07)
# Updated date: (2023-11-07)
# Updated date: (2023-11-07)
# Updated date: (2023-11-07)
# Updated date: (2023-11-07)
# Updated date: (2023-11-07)
# Updated date: (2023-11-07)
# Updated date: (2023-11-08)
# Updated date: (2023-11-08)
# Updated date: (2023-11-09)
# Updated date: (2023-11-10)
# Updated date: (2023-11-10)
# Updated date: (2023-11-10)
# Updated date: (2023-11-10)
# Updated date: (2023-11-10)
# Updated date: (2023-11-10)
# Updated date: (2023-11-10)
# Updated date: (2023-11-11)
# Updated date: (2023-11-11)
# Updated date: (2023-11-11)
# Updated date: (2023-11-11)
# Updated date: (2023-11-11)
# Updated date: (2023-11-11)
# Updated date: (2023-11-12)
# Updated date: (2023-11-13)
# Updated date: (2023-11-14)
# Updated date: (2023-11-14)
# Updated date: (2023-11-15)
# Updated date: (2023-11-16)
# Updated date: (2023-11-17)
# Updated date: (2023-11-18)
# Updated date: (2023-11-18)
# Updated date: (2023-11-19)
# Updated date: (2023-11-19)
# Updated date: (2023-11-20)
# Updated date: (2023-11-21)
# Updated date: (2023-11-22)
# Updated date: (2023-11-23)
# Updated date: (2023-11-24)
# Updated date: (2023-11-26)
# Updated date: (2023-11-26)
# Updated date: (2023-11-27)
# Updated date: (2023-11-28)
# Updated date: (2023-11-29)
# Updated date: (2023-11-30)
# Updated date: (2023-12-01)
# Updated date: (2023-12-01)
# Updated date: (2023-12-02)
# Updated date: (2023-12-02)
# Updated date: (2023-12-03)
# Updated date: (2023-12-03)
# Updated date: (2023-12-04)
# Updated date: (2023-12-05)
# Updated date: (2023-12-06)
# Updated date: (2023-12-11)
# Updated date: (2023-12-12)
# Updated date: (2023-12-14)
# Updated date: (2023-12-15)
# Updated date: (2023-12-15)
# Updated date: (2023-12-16)
# Updated date: (2023-12-19)
# Updated date: (2023-12-20)
# Updated date: (2023-12-20)
# Updated date: (2023-12-21)
# Updated date: (2023-12-24)
# Updated date: (2023-12-27)
# Updated date: (2023-12-27)
# Updated date: (2023-12-28)
# Updated date: (2023-12-28)
# Updated date: (2023-12-29)
# Updated date: (2023-12-29)
# Updated date: (2023-12-30)
# Updated date: (2023-12-31)
# Updated date: (2023-12-31)
# Updated date: (2024-01-02)
# Updated date: (2024-01-02)
# Updated date: (2024-01-03)
# Updated date: (2024-01-03)
# Updated date: (2024-01-04)
# Updated date: (2024-01-04)
# Updated date: (2024-01-05)
# Updated date: (2024-01-06)
# Updated date: (2024-01-07)
# Updated date: (2024-01-08)
# Updated date: (2024-01-08)
# Updated date: (2024-01-08)
# Updated date: (2024-01-09)
# Updated date: (2024-01-09)
# Updated date: (2024-01-10)
# Updated date: (2024-01-10)
# Updated date: (2024-01-10)
# Updated date: (2024-01-11)
# Updated date: (2024-01-11)
# Updated date: (2024-01-11)
# Updated date: (2024-01-12)
# Updated date: (2024-01-12)
# Updated date: (2024-01-13)
# Updated date: (2024-01-13)
# Updated date: (2024-01-14)
# Updated date: (2024-01-14)
# Updated date: (2024-01-15)
# Updated date: (2024-01-15)
# Updated date: (2024-01-16)
# Updated date: (2024-01-17)
# Updated date: (2024-01-18)
# Updated date: (2024-01-18)
# Updated date: (2024-01-19)
# Updated date: (2024-01-22)
# Updated date: (2024-01-22)
# Updated date: (2024-01-23)
# Updated date: (2024-01-23)
# Updated date: (2024-01-24)
# Updated date: (2024-01-24)
# Updated date: (2024-01-25)
# Updated date: (2024-01-26)
# Updated date: (2024-01-26)
# Updated date: (2024-01-27)
# Updated date: (2024-01-28)
# Updated date: (2024-01-28)
# Updated date: (2024-01-29)
# Updated date: (2024-01-29)
# Updated date: (2024-02-02)
# Updated date: (2024-02-02)
# Updated date: (2024-02-04)
# Updated date: (2024-02-05)
# Updated date: (2024-02-07)
# Updated date: (2024-02-10)
# Updated date: (2024-02-14)
# Updated date: (2024-02-15)
# Updated date: (2024-02-16)
# Updated date: (2024-02-16)
# Updated date: (2024-02-17)
# Updated date: (2024-02-17)
# Updated date: (2024-02-18)
# Updated date: (2024-02-18)
# Updated date: (2024-02-19)
# Updated date: (2024-02-20)
# Updated date: (2024-02-21)
# Updated date: (2024-02-22)
# Updated date: (2024-02-22)
# Updated date: (2024-02-23)
# Updated date: (2024-02-23)
# Updated date: (2024-02-24)
# Updated date: (2024-02-25)
# Updated date: (2024-02-25)
# Updated date: (2024-02-25)
# Updated date: (2024-02-26)
# Updated date: (2024-02-27)
# Updated date: (2024-02-28)
# Updated date: (2024-02-29)
# Updated date: (2024-03-01)
# Updated date: (2024-03-02)
# Updated date: (2024-03-02)
# Updated date: (2024-03-02)
# Updated date: (2024-03-04)
# Updated date: (2024-03-06)
# Updated date: (2024-03-06)
# Updated date: (2024-03-07)
# Updated date: (2024-03-08)
# Updated date: (2024-03-09)
# Updated date: (2024-03-09)
# Updated date: (2024-03-10)
# Updated date: (2024-03-10)
# Updated date: (2024-03-10)
# Updated date: (2024-03-11)
# Updated date: (2024-03-12)
# Updated date: (2024-03-12)
# Updated date: (2024-03-13)
# Updated date: (2024-03-13)
# Updated date: (2024-03-16)
# Updated date: (2024-03-17)
# Updated date: (2024-03-20)
# Updated date: (2024-03-21)
# Updated date: (2024-03-22)
# Updated date: (2024-03-23)
# Updated date: (2024-03-24)
# Updated date: (2024-03-24)
# Updated date: (2024-03-25)
# Updated date: (2024-03-30)
# Updated date: (2024-03-31)
# Updated date: (2024-04-01)
# Updated date: (2024-04-01)
# Updated date: (2024-04-01)
# Updated date: (2024-04-02)
# Updated date: (2024-04-02)
# Updated date: (2024-04-03)
# Updated date: (2024-04-07)
# Updated date: (2024-04-09)
# Updated date: (2024-04-11)
# Updated date: (2024-04-11)
# Updated date: (2024-04-12)
# Updated date: (2024-04-12)
# Updated date: (2024-04-13)
# Updated date: (2024-04-13)