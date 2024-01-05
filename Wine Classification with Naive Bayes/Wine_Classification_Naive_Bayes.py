#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 23:30:59 2023

@author: juanhuerta
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix

# Step 1: Reading the dataset
file_path = '/Users/juanhuerta/Desktop/INFS3325/wine4.csv'  # Replace with your file path
myData_DF = pd.read_csv(file_path)

# Sorting the dataframe on the 'class' column
myData_sorted_DF = myData_DF.sort_values(by='class')

# Creating the X and y variables
X = myData_sorted_DF.drop('class', axis=1)
y = myData_sorted_DF['class']

# Step 2: Splitting the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Counting the number of classes in the test set
count_class_1 = (y_test == 1).sum()
count_class_2 = (y_test == 2).sum()

# Printing counts
print(f"Number of rows classified as grape variety 1 in test set: {count_class_1}")
print(f"Number of rows classified as grape variety 2 in test set: {count_class_2}")

# Step 3: Training the model
gnb = GaussianNB()
gnb.fit(X_train, y_train)

# Making predictions
y_pred = gnb.predict(X_test)

# Step 4: Model evaluation
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")

# Confusion matrix
myMatrix = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(myMatrix)

# Labeled confusion matrix
pred_labels = ['pred class 1', 'pred class 2']
row_labels = ['actual class 1', 'actual class 2']
confusion_DF = pd.DataFrame(myMatrix, index=row_labels, columns=pred_labels)
print(confusion_DF)

# Extracting values for reporting
true_class_1 = myMatrix[0][0]
false_class_2_as_1 = myMatrix[1][0]
true_class_2 = myMatrix[1][1]
false_class_1_as_2 = myMatrix[0][1]

# Printing results
print(f"True predictions of type 1 grapes: {true_class_1}")
print(f"False predictions of type 1 grapes: {false_class_2_as_1}")
print(f"True predictions of type 2 grapes: {true_class_2}")
print(f"False predictions of type 2 grapes: {false_class_1_as_2}")
