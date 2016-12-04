import pandas as pd
import quandl # https://www.quandl.com/

df = quandl.get('WIKI/GOOGL')

print(df.head())

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
