#!/usr/bin/env python
# coding: utf-8

# In[35]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[36]:


#Analysing Closing price of Stocks and VOlume trading


# In[37]:


path = r'C:\Users\HP\Downloads\individual_stocks_5yr-20210927T085011Z-001\individual_stocks_5yr'
company_list = ['AAPL_data.csv','GOOG_data.csv','MSFT_data.csv','AMZN_data.csv']
all_data = pd.DataFrame()
for file in company_list:
    current_df = pd.read_csv(path+ '/' + file)
    all_data = pd.concat([all_data, current_df])
all_data.shape    


# In[38]:


all_data.head()


# In[39]:


all_data.dtypes


# In[40]:


all_data['date'] = pd.to_datetime(all_data['date'])


# In[41]:


all_data.dtypes


# In[42]:


tech_list = all_data['Name'].unique()


# In[43]:


plt.figure(figsize=(20,12))
for i,company in enumerate(tech_list,1):
    plt.subplot(2,2,i)
    df = all_data[all_data['Name']==company]
    plt.plot(df['date'],df['close'])
    plt.xticks(rotation='vertical')
    plt.title(company)


# In[44]:


import plotly.express as px


# In[45]:


for company in tech_list:
    df = all_data[all_data['Name']==company]
    fig = px.line(df,x='date',y='volume',title=company)
    fig.show()


# In[46]:


#Analysing Daily Returns


# In[47]:


df = pd.read_csv(r'C:\Users\HP\Downloads\individual_stocks_5yr-20210927T085011Z-001\individual_stocks_5yr/AAPL_data.csv')
df.head()


# In[48]:


df['Daily_Price_change'] = df['close']-df['open']
df.head()


# In[49]:


df['1day % return'] = ((df['close']-df['open'])/df['close'])*100
df.head()


# In[50]:


fig = px.line(df,x='date',y='1day % return',title=company)
fig.show()


# In[51]:


df2 = df.copy()


# In[52]:


df2.dtypes


# In[53]:


df2['date'] = pd.to_datetime(df2['date'])


# In[54]:


df2.set_index('date', inplace=True)


# In[55]:


df2.head()


# In[56]:


df2['2013-02-08':'2013-02-14']


# In[57]:


df2['close'].resample('M').mean().plot()


# In[58]:


df2['close'].resample('Y').mean().plot(kind='bar')


# In[59]:


#Performing multi variate analysis


# In[60]:


appl = pd.read_csv(r'C:\Users\HP\Downloads\individual_stocks_5yr-20210927T085011Z-001\individual_stocks_5yr/AAPL_data.csv')
appl.head()


# In[61]:


amzn = pd.read_csv(r'C:\Users\HP\Downloads\individual_stocks_5yr-20210927T085011Z-001\individual_stocks_5yr/AMZN_data.csv')
amzn.head()


# In[62]:


msft = pd.read_csv(r'C:\Users\HP\Downloads\individual_stocks_5yr-20210927T085011Z-001\individual_stocks_5yr/MSFT_data.csv')
msft.head()


# In[63]:


goog = pd.read_csv(r'C:\Users\HP\Downloads\individual_stocks_5yr-20210927T085011Z-001\individual_stocks_5yr/GOOG_data.csv')
goog.head()


# In[64]:


close = pd.DataFrame()


# In[65]:


close['appl'] = appl['close']
close['goog'] = goog['close']
close['amzn'] = amzn['close']
close['msft'] = msft['close']


# In[66]:


close.head()


# In[67]:


import seaborn as sns


# In[68]:


sns.pairplot(data=close)


# In[74]:


sns.heatmap(close.corr(), annot=True)


# In[75]:


appl.head()


# In[76]:


data = pd.DataFrame()


# In[78]:


data['appl_change'] = ((appl['close'] - appl['open'])/appl['close'])*100
data['goog_change'] = ((goog['close'] - goog['open'])/goog['close'])*100
data['amzn_change'] = ((amzn['close'] - amzn['open'])/amzn['close'])*100
data['msft_change'] = ((msft['close'] - msft['open'])/msft['close'])*100


# In[79]:


data.head()


# In[80]:


sns.pairplot(data=data)


# In[81]:


sns.heatmap(data.corr(), annot=True)


# In[82]:


#value at risk analysis


# In[84]:


sns.displot(data['appl_change'])


# In[85]:


data['appl_change'].std()
#### 68% of entire data


# In[86]:


data['appl_change'].std()*2
#### 95% of entire data


# In[87]:


data['appl_change'].std()*3
#### 99.7% of entire data


# In[88]:


data['appl_change'].quantile(0.1)


# In[89]:


data.describe().T


# In[ ]:




