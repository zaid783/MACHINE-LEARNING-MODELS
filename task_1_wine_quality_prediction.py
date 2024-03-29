# -*- coding: utf-8 -*-
"""Task 1 Wine Quality Prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_T1tckdIkXoq1yT3wn9yKSrf2Os6wBx5
"""



"""Importing the Dependencies"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score



"""Data Collection Part

"""

#loading dataset into panda frame
wine_dataset = pd.read_csv('/content/winequality-red.csv')

#number of rows and column in data set
wine_dataset.shape

#first five rows of data set
wine_dataset.head()

#checking for missing values
wine_dataset.isnull().sum()



"""Data Anylsis And Visualization"""

wine_dataset.describe()

#number of values for each quality
sns.catplot(x="quality",data=wine_dataset,kind="count")

# volatile accidty VS Quality
plot = plt.figure(figsize=(5,5))
sns.barplot(x="quality",y="volatile acidity", data = wine_dataset)

# citric acid VS Quality
plot = plt.figure(figsize=(5,5))
sns.barplot(x="quality",y="citric acid", data = wine_dataset)

# residual sugar VS Quality
plot = plt.figure(figsize=(5,5))
sns.barplot(x="quality",y="residual sugar", data = wine_dataset)



"""Correlation

"""

correlation = wine_dataset.corr()

#constructing the heatmap for understanding the correlation between the columns.
plt.figure(figsize=(10,10))
sns.heatmap(correlation, cbar=True, square=True ,fmt=".1f", annot=True, annot_kws={"size":8}, cmap="Blues")



"""Data PreProcessing"""

X = wine_dataset.drop("quality",axis=1)

print(X)



"""Label Binarization

"""

Y = wine_dataset["quality"].apply(lambda y_value: 1 if y_value>=7 else 0)

print(Y)

X_train , X_test , Y_train , Y_test = train_test_split(X, Y, test_size=0.2, random_state=3)

print(Y.shape, Y_train.shape, Y_test.shape)



"""Model Training (Random Forest)"""

model = RandomForestClassifier()

model.fit(X_train, Y_train)



"""Model Evaluation"""

#accuracy on test data
X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)

print("Accuracy : ", test_data_accuracy)



"""Building A Predictive System Of Wine"""

# input_data = (7.3,0.65,0.0,1.2,0.065,15.0,21.0,0.9946,3.39,0.47,10.0)#this for good quality because if we run this end value is equal to 7 so that's why this is good quality.
input_data=(8.1,0.56,0.28,1.7,0.368,16.0,56.0,0.9968,3.11,1.28,9.3)#this one i bad qualtiy beacuse in this the end value is equal to 5 so, that's why this is bad qualtiy.
input_data_as_numpy_array = np.asarray(input_data)
#reshape the data for predicting the label for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
prediction = model.predict(input_data_reshaped)
print(prediction)

if(prediction[0]==1):
  print("Good Quality")
else:
  print("Bad Quality")

