import sqlite3
import plotly.express as px
import pandas as pd
import json
from datetime import datetime

# Database Connection
path_for_database = r'C:\Users\raviteja.matla\Downloads\pycharm files\Stocks_json.db'
connect = sqlite3.connect(path_for_database)
cursor = connect.cursor()

# Using JSON file created the data
path_for_data = r'C:\Users\raviteja.matla\Downloads\pycharm files\AllStocks.json'
with open(path_for_data) as json_f:
    dataset = json.load(json_f)


# Class to create table and insert data
class create_data:
    def __init__(self, symbol, date, value):
        self.symbol = symbol
        self.date = date
        self.value = value

    def create_table(self):
        stock_table = " CREATE TABLE IF NOT EXISTS [" + self.symbol
        stock_table = stock_table + "] ( Date date PRIMARY KEY," + self.symbol + " real NOT NULL ) "
        cursor.execute(stock_table)

    def insert_data(self):
        insert_data = 'INSERT or IGNORE INTO ' + self.symbol + " VALUES ('"
        insert_data = insert_data + str(self.date)
        insert_data = insert_data + " ',' " + str(self.value) + "' );"
        cursor.execute(insert_data)


# stock data
stockSbls = ['GOOG', 'AIG', 'MSFT', 'RDSA', 'FB', 'M', 'F', 'IBM']
stock_dict = {'GOOG': 25, 'AIG': 235, 'MSFT': 85, 'RDS-A': 400, 'FB': 130, 'M': 425, 'F': 85, 'IBM': 80}

# loop to create table for each stock
for data in dataset:
    try:
        stockDate = datetime.strptime(data['Date'], '%d-%b-%y')
    except ValueError:
        print('Date format of this stock is not correct')
        stockVal = round(data['Close'] * stock_dict[data['Symbol']], 2)
        newStock = create_data(data['Symbol'], stockDate, stockVal)
        newStock.create_table()
        newStock.insert_data()

# Merge individual stocks into single df
selecting_dates = "SELECT Date FROM AIG"
df_all_stocks = pd.read_sql_query(selecting_dates, connect)
for stock in stockSbls:
    select_table = "SELECT * from " + stock
    df_name = stock + '_df'
    df_name = pd.read_sql_query(select_table, connect)
    df_all_stocks = pd.merge(df_all_stocks, df_name, how='left', on=["Date"])

# Creating graph using plotly
figure = px.line(df_all_stocks, x="Date", y=df_all_stocks.columns,
              hover_data={"Date": "|%Y,%m,%d"},
              title=' Stock Portfolio')
figure.update_xaxes(dtick="M1", tickformat="%b\n%Y")
figure.show()

# Database Commit and Close
connect.commit()
connect.close()


