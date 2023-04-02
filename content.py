#!/usr/bin/env python
# coding: utf-8

# In[40]:


import pandas as pd
import numpy
from sklearn import linear_model

data = pd.read_excel(r"C:/Users/anies/Downloads/HousePricePrediction.xlsx")
data=data.dropna()


# In[42]:
# In[41]:


x = data.iloc[:,:-1].values
y = data.iloc[:,-1].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state =0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)
y_predict = regressor.predict(X_test)

# In[41
import pickle

pickle.dump(regressor,open('model.pkl','wb'))
# In[ ]:




