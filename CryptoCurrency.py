import warnings
warnings.filterwarnings('ignore')
import numpy as np 
import pandas as pd 
from pandas import DataFrame
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
#from matplotlib.finance import candlestick_ohlc
import seaborn as sns
#importing packages for the prediction of time-series data

from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import pandas as pd

#configuring the Environment
color = sns.color_palette()
%matplotlib inline

pd.options.mode.chained_assignment = None
pd.options.display.max_columns = 999


crypto_data = {}

#crypto_data['bitcoin'] = pd.read_csv('./input/bitcoin_price.csv', parse_dates=['Date'])
#crypto_data['bitcoin_cash'] = pd.read_csv("./input/bitcoin_cash_price.csv", parse_dates=['Date'])
#crypto_data['dash'] = pd.read_csv("./input/dash_price.csv", parse_dates=['Date'])
#crypto_data['ethereum'] = pd.read_csv("./input/ethereum_price.csv", parse_dates=['Date'])
#crypto_data['iota'] = pd.read_csv("./input/iota_price.csv", parse_dates=['Date'])
#crypto_data['litecoin'] = pd.read_csv("./input/litecoin_price.csv", parse_dates=['Date'])
#crypto_data['monero'] = pd.read_csv("./input/monero_price.csv", parse_dates=['Date'])
#crypto_data['nem'] = pd.read_csv("./input/nem_price.csv", parse_dates=['Date'])
#crypto_data['neo'] = pd.read_csv("./input/neo_price.csv", parse_dates=['Date'])
#crypto_data['numeraire'] = pd.read_csv("./input/numeraire_price.csv", parse_dates=['Date'])
#crypto_data['ripple'] = pd.read_csv("./input/ripple_price.csv", parse_dates=['Date'])
#crypto_data['stratis'] = pd.read_csv("./input/stratis_price.csv", parse_dates=['Date'])
#crypto_data['waves'] = pd.read_csv("./input/waves_price.csv", parse_dates=['Date'])
crypto_data = pd.read_csv("./CryptoDataSet/eth.csv")




#MAximum price by  year from 1970 to  2019
#Convert string date to Datetime  

crypto_data['date'] = pd.to_datetime(crypto_data['date'])
#Extract year from Date 
crypto_data['date'] = pd.DatetimeIndex(crypto_data['date']).year
#print(crypto_data)

maxprice=crypto_data.groupby(['date'], sort=False)['price'].max()
print(maxprice)


#MAximum price by  year from 1970 to  2019
#Convert string date to Datetime  
crypto_data = pd.read_csv("./CryptoDataSet/eth.csv")

crypto_data['date'] = pd.to_datetime(crypto_data['date'])
#Extract day from Date 
crypto_data['date'] = pd.DatetimeIndex(crypto_data['date']).month
#print(crypto_data)

maxdayprice=crypto_data.groupby(['date'], sort=False)['price'].max()
maxblockSize=crypto_data.groupby(['date'], sort=False)['blockSize'].max()
maxblockCount=crypto_data.groupby(['date'], sort=False)['blockCount'].max()
print(maxdayprice.sort_values('price', ascending=False))
print(maxblockSize.sort_values('blockSize', ascending=False))
print(maxblockCount.sort_values('blockCount', ascending=False))



# a simple line plot
crypto_data.plot(kind='bar',x='date',y='price')
