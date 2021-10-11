import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

#Analysing Closing price of Stocks and Volume trading
path = r'C:\Users\HP\Downloads\individual_stocks_5yr-20210927T085011Z-001\individual_stocks_5yr'
company_list = ['AAPL_data.csv','GOOG_data.csv','MSFT_data.csv','AMZN_data.csv']
all_data = pd.DataFrame()
for file in company_list:
    current_df = pd.read_csv(path+ '/' + file)
    all_data = pd.concat([all_data, current_df])
all_data.shape    
all_data.head()
all_data.dtypes

all_data['date'] = pd.to_datetime(all_data['date'])
all_data.dtypes

tech_list = all_data['Name'].unique()

plt.figure(figsize=(20,12))
for i,company in enumerate(tech_list,1):
    plt.subplot(2,2,i)
    df = all_data[all_data['Name']==company]
    plt.plot(df['date'],df['close'])
    plt.xticks(rotation='vertical')
    plt.title(company)

for company in tech_list:
    df = all_data[all_data['Name']==company]
    fig = px.line(df,x='date',y='volume',title=company)
    fig.show()

#Analysing Daily Returns
df = pd.read_csv(r'C:\Users\HP\Downloads\individual_stocks_5yr-20210927T085011Z-001\individual_stocks_5yr/AAPL_data.csv')
df.head()

df['Daily_Price_change'] = df['close']-df['open']
df.head()

df['1day % return'] = ((df['close']-df['open'])/df['close'])*100
df.head()

fig = px.line(df,x='date',y='1day % return',title=company)
fig.show()

df2 = df.copy()
df2.dtypes
df2['date'] = pd.to_datetime(df2['date'])
df2.set_index('date', inplace=True)
df2.head()
df2['2013-02-08':'2013-02-14']
df2['close'].resample('M').mean().plot()
df2['close'].resample('Y').mean().plot(kind='bar')

#Performing multi variate analysis
appl = pd.read_csv(r'C:\Users\HP\Downloads\individual_stocks_5yr-20210927T085011Z-001\individual_stocks_5yr/AAPL_data.csv')
appl.head()

amzn = pd.read_csv(r'C:\Users\HP\Downloads\individual_stocks_5yr-20210927T085011Z-001\individual_stocks_5yr/AMZN_data.csv')
amzn.head()

msft = pd.read_csv(r'C:\Users\HP\Downloads\individual_stocks_5yr-20210927T085011Z-001\individual_stocks_5yr/MSFT_data.csv')
msft.head()

goog = pd.read_csv(r'C:\Users\HP\Downloads\individual_stocks_5yr-20210927T085011Z-001\individual_stocks_5yr/GOOG_data.csv')
goog.head()

close = pd.DataFrame()
close['appl'] = appl['close']
close['goog'] = goog['close']
close['amzn'] = amzn['close']
close['msft'] = msft['close']
close.head()

sns.pairplot(data=close)
sns.heatmap(close.corr(), annot=True)

appl.head()
data = pd.DataFrame()

data['appl_change'] = ((appl['close'] - appl['open'])/appl['close'])*100
data['goog_change'] = ((goog['close'] - goog['open'])/goog['close'])*100
data['amzn_change'] = ((amzn['close'] - amzn['open'])/amzn['close'])*100
data['msft_change'] = ((msft['close'] - msft['open'])/msft['close'])*100
data.head()

sns.pairplot(data=data)
sns.heatmap(data.corr(), annot=True)

#value at risk analysis
sns.displot(data['appl_change'])

data['appl_change'].std()
#### 68% of entire data

data['appl_change'].std()*2
#### 95% of entire data

data['appl_change'].std()*3
#### 99.7% of entire data

data['appl_change'].quantile(0.1)
data.describe().T
