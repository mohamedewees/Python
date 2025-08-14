import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from tabulate import tabulate
from sklearn.metrics import mean_squared_error, mean_absolute_error, root_mean_squared_error , r2_score

df = pd.read_csv(r'D:\NVIDIA AI Course\Udemy_NVIDIA-Certified_Associate_Generative_AI_LLMs_NCA-GENL_2025-1_Downloadly.ir\Advertising.csv')
# print(tabulate(df.head(),headers = 'keys',tablefmt = 'fancy_grid'))

# drop unnamed column as it is useless
#inlace=True means we will drop this column permanently in the original df
df.drop(columns='Unnamed: 0',inplace=True)
# print(tabulate(df.head(),headers = 'keys',tablefmt = 'fancy_grid'))

# Mathematical representation of linear regression is (y = a + bx) where a is called y-interceptor and b is called slope and x is the feature.
# in case we have multiple features, then the equation would be like this (Y= θ0+ θ1X1+θ2X2,….) where x1,x2 are called features,
# θ0 is the intercept and (θ1,θ2,θn) are coefficient

# let's assign the features and target
features_columns = ['TV','radio','newspaper']
X = df[features_columns]
y = df['sales']


#first let's split the data into 70% train and 30% test
X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=4,test_size=0.3)
print(X_train.shape)
print(X_test.shape)

# feed the model to get a trained model
lr = LinearRegression()
lr.fit(X_train,y_train)

# get coefficients and interceptor
print(lr.coef_)
print(lr.intercept_)

#generate the predicted data
y_pred = lr.predict(X_test)
print(y_pred[:5])

#Evaluation of the model to detect how the model perform
# there are many evaluation functions like:
# mean absolute error
# mean squared error
# Root mean squared error
# R2 score

print(f"MAE is: {mean_absolute_error(y_test,y_pred)}")
print(f"MSE is: {mean_squared_error(y_test,y_pred)}")
# print(f"RMSE is: {mean_squared_error(y_test,y_pred, squared = False)}")
print(f"RMSE is: {root_mean_squared_error(y_test,y_pred)}")

# R2 score means how much variance can be explained by the given features
print(f"R2 Score is: {r2_score(y_test,y_pred)}")