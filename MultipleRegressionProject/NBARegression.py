import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.feature_selection import f_regression


df = pd.read_csv("MultipleRegressionProject/BallTeamStats.csv")
# df.drop( 'Rk' , inplace = True,axis=1)
print(df.head())

# print(df.head())
# print(df.columns)


X = df[['Age', 'MOV', 'SOS', 'ORtg', 'DRtg', 'Pace',
 'FTr', '3PAr', 'TS%', 'eFG%', 'TOV%', 'ORB%', 'FT/FGA',
  'D_eFG%', 'D_TOV%', 'D_RB%', 'D_FT/FGA']]
y = df['W']

arrPar = ['Age', 'MOV', 'SOS', 'ORtg', 'DRtg', 'Pace',
 'FTr', '3PAr', 'TS%', 'eFG%', 'TOV%', 'ORB%', 'FT/FGA',
  'D_eFG%', 'D_TOV%', 'D_RB%', 'D_FT/FGA']

for i in arrPar:
  sns.scatterplot(x=i, y='W', data=df)
  plt.show()



X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=None)

model = LinearRegression()

model.fit(X_train,y_train)

predictions = model.predict(X_test)

finalPredict = model.predict([[27.5,7.5,-0.56,114.8,107.3,99.8,0.221,0.354,0.581,0.549,11.6,22.3,0.176,0.51,13,77.1,0.195,]])
print(finalPredict)

print(
  'mean_squared_error : ', mean_squared_error(y_test, predictions))
print(
  'mean_absolute_error : ', mean_absolute_error(y_test, predictions))


import statsmodels.api as ssm #for detail description of linear coefficients, intercepts, deviations, and many more

X=ssm.add_constant(X)        #to add constant value in the model
model= ssm.OLS(y,X).fit()         #fitting the model
print(model.summary())
