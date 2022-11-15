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


df = pd.read_csv("MultipleRegressionProject\Real-estate1.csv")
df.drop('No', inplace = True,axis=1)

# print(df.head())
# print(df.columns)

sns.scatterplot(x='X4 number of convenience stores',
                y='Y house price of unit area', data=df)

plt.show()


X = df.drop('Y house price of unit area',axis= 1)
y = df['Y house price of unit area']
print(X)
print(y)


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=101)

model = LinearRegression()

model.fit(X_train,y_train)

predictions = model.predict(X_test)

print(
  'mean_squared_error : ', mean_squared_error(y_test, predictions))
print(
  'mean_absolute_error : ', mean_absolute_error(y_test, predictions))
print(
  df.describe())

# model.fit(X_train,y_train)
# soloPredict = model.predict([[2013.333,6.3,90.45606,9,24.97433,121.5431]])



dataRefUrl = 'https://www.nba.com/stats/teams/advanced?Season=2021-22&dir=A&sort=PACE'