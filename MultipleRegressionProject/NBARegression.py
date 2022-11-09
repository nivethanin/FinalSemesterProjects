import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn import preprocessing

df = pd.read_csv('Real estate.csv')
df.drop('No', inplace = True,axis=1)
  
print(df.head())
print(df.columns)