'''

# For each stock, make a separate dataframe and include a value-calculating column.
# Attached .copy() at the end to avoid "SettingWithCopyWarning"
AIG_dframe = r_stocks[r_stocks['Symbol'] == 'AIG'].copy()
AIG_dframe['Value'] = AIG_dframe.Close*235

GOOGL_dframe = r_stocks[r_stocks['Symbol'] == 'GOOGL'].copy()
GOOGL_dframe['Value'] = GOOGL_dframe.Close*125


MSFT_dframe = r_stocks[r_stocks['Symbol'] == 'MSFT'].copy()
MSFT_dframe['Value'] = MSFT_dframe.Close*85

RDSA_dframe = r_stocks[r_stocks['Symbol'] == 'RDS-A'].copy()
RDSA_dframe['Value'] = RDSA_dframe.Close*400

FB_dframe = r_stocks[r_stocks['Symbol'] == 'FB'].copy()
FB_dframe['Value'] = FB_dframe.Close*130

M_dframe = r_stocks[r_stocks['Symbol'] == 'M'].copy()
M_dframe['Value'] = M_dframe.Close*425

F_dframe = r_stocks[r_stocks['Symbol'] == 'F'].copy()
F_dframe['Value'] = F_dframe.Close*85

IBM_dframe = r_stocks[r_stocks['Symbol'] == 'IBM'].copy()
IBM_dframe['Value'] = IBM_dframe.Close*80


# Graph each stock.
plt.figure(figsize=(15, 8))
plt.plot(AIG_dframe['Date'], AIG_dframe['Value'], label='AIG')
plt.plot(GOOGL_dframe['Date'], GOOGL_dframe['Value'], label='GOOGL')
plt.plot(MSFT_dframe['Date'], MSFT_dframe['Value'], label='MSFT')
plt.plot(RDSA_dframe['Date'], RDSA_dframe['Value'], label='RDSA')
plt.plot(FB_dframe['Date'], FB_dframe['Value'], label='FB')
plt.plot(M_dframe['Date'], M_dframe['Value'], label='M')
plt.plot(F_dframe['Date'], F_dframe['Value'], label='F')
plt.plot(IBM_dframe['Date'], IBM_dframe['Value'], label='IBM')

# make a legend and record the story in a file
plt.legend(loc='upper left')
plt.savefig('simplePlot.png')

'''
# Ravi Teja Matla
# 7th august 2022
# Stocks with Data visualization

import pandas as pd
import matplotlib.pyplot as plt
import plotly.offline as pyo
import plotly.graph_objs as go
import json
import plotly.express as px

# Assigning a variable to store file path
f_path = r'C:\Users\raviteja.matla\Downloads\pycharm files\AllStocks.json'

# Assigning a variable to read the json file
r_stocks = pd.read_json(f_path)

with open(f_path) as f:
    data = json.load(f)
    count = len(data)
    AIG_data = []
    GOOG_data = []
    MSFT_data = []
    RDSA_data = []
    FB_data = []
    M_data = []
    F_data = []
    IBM_data = []
    for x in range(count):
        if data[x]['Symbol'] == 'AIG':
            AIG_data.append(data[x]['Close'])
        elif data[x]['Symbol'] == 'GOOG':
            GOOG_data.append(data[x]['Close'])
        elif data[x]['Symbol'] == 'MSFT':
            MSFT_data.append(data[x]['Close'])
        elif data[x]['Symbol'] == 'RDS-A':
            RDSA_data.append(data[x]['Close'])
        elif data[x]['Symbol'] == 'FB':
            FB_data.append(data[x]['Close'])
        elif data[x]['Symbol'] == 'M':
            M_data.append(data[x]['Close'])
        elif data[x]['Symbol'] == 'F':
            F_data.append(data[x]['Close'])
        elif data[x]['Symbol'] == 'IBM':
            IBM_data.append(data[x]['Close'])

df = px.data.gapminder().query("continent == 'Oceania'")
fig = px.line(df, x='year', y='lifeExp', color='country', symbol="country")
fig.show()



