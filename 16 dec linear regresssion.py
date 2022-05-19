# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 14:18:09 2021

@author: lenovo
"""

import pandas as pd
import numpy as np

df=pd.read_csv(r"C:\Users\lenovo\OneDrive\Desktop\harman's folder\ML AND AI\insurance.csv")
 
# Simple Linear Regression

X = df.iloc[:, :-1]
y = df.iloc[:, -1]

from sklearn.preprocessing import LabelEncoder
gender = LabelEncoder()
X["gender"] = gender.fit_transform(X["gender"])

smoker=LabelEncoder()
X["smoker"]=smoker.fit_transform(X["smoker"])

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

ct=ColumnTransformer(transformers=[("Encoding",OneHotEncoder(),[5])],remainder="passthrough")
X=ct.fit_transform(X)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X=sc.fit_transform(X)


# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)


from sklearn.linear_model import LinearRegression
regressor =LinearRegression()
regressor.fit(X_train,y_train)


y_pred=regressor.predict(X_test)

from sklearn.metrics import r2_score
print(r2_score(y_test,y_pred))
#if r2 score is nearer to 1 then model is more efficient
#hyperparameter tuning : regressor =LinearRegression(fit_intercept=False or fit_intercept=True)
#r2 score ranger between minus infinity to 1


user=pd.DataFrame({'age':[int(input('Enter your age'))],'gender':[input('Enter your gender')],
                   'bmi':[float(input('Enter bmi'))],'children':[int(input('Enter children'))],
                   'smoker':[input('Enter wether you smoke /not?')],'region':[input('Enter area')]})
user['gender']=gender.transform(user['gender'])

user['smoker']=smoker.transform(user['smoker'])

user=ct.transform(user)

user=sc.transform(user)


print('You charges are:',regressor.predict(abs(user)))








