####################################################
##	IMPORTING MODULES
####################################################

import pandas as pd
import quandl # https://www.quandl.com/
import math
import numpy as np
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression

####################################################
##	GETTING DATA
####################################################

# querying google stock data from quandl
df = quandl.get('WIKI/GOOGL', authtoken="THwLbb9rbGjxWnWp84sU")
print(df.head())
dataFile = 'googleStock-quandl.csv'
df.to_csv(dataFile, sep='\t', encoding='utf-8')

####################################################
##	TRANSFORMING DATA
####################################################

# specifying desired columns for working dataframe
df = df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume',]]
# high_low_percent_change = (adjusted_high - adjusted_close) / (adjusted close = 100)
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100.0
# percent_change = (adjusted_close - adjusted_open) / (adjusted_open * 100)
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0
# specifying better columns for working dataframe
df = df[['Adj. Close','HL_PCT','PCT_change','Adj. Volume',]]
# declaring forecast variable
forecast_col = 'Adj. Close'
# dealing with null values
df.fillna(-9999, inplace = True)
# specifying length of prediction output
forecast_out = int(math.ceil(0.01 * len(df)))
df['label'] = df[forecast_col].shift(-forecast_out)
df.dropna(inplace = True)
print(df.head())
dataFile = 'googleStock_forecast.csv'
df.to_csv(dataFile, sep='\t', encoding='utf-8')




