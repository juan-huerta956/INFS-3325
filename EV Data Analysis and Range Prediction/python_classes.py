#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Juan Huerta
Date of Creation: Sat Dec 9 13:59:46 2023
INFS 3325: '/Users/juanhuerta/Desktop/INFS3325'

Description:
This program is designed to analyze a dataset containing 
electric vehicle (EV) specifications and prices. It encapsulates 
the functionality within a class called 'EVData' for structured data analysis.

Inputs: 
- 'dataset_name': A string representing the name of the dataset.
- 'dataset_path': A string specifying the local file path to the dataset.
- 'dataset_url': A string containing the URL from which the dataset can be obtained.

Processing: 
- The program loads the dataset from the specified 'dataset_path' into a pandas DataFrame.
- It provides methods to describe individual columns, calculate correlations
  between columns, and perform simple linear regression analysis.
- The class ensures data integrity and provides well-formatted output.

Outputs: 
- Descriptive statistics for selected columns in the dataset.
- Correlation matrix between selected columns.
- Coefficients and intercept for a simple linear regression model.

"""


import pandas as pd

# Step 1: Define the EVData class to encapsulate dataset-related functionality.
class EVData:
    def __init__(self, dataset_name, dataset_path, dataset_url):
        # Step 3a: Initialize instance variables for meta-information.
        self.dataset_name = dataset_name
        self.dataset_path = dataset_path
        self.dataset_url = dataset_url
        self.num_rows = None
        self.num_columns = None
        self._data = None

    # Step 3b: Create a method to load data from the specified path.
    def load_data(self):
        self._data = pd.read_csv(self.dataset_path)
        self.num_rows, self.num_columns = self._data.shape

    # Step 3c: Implement a getter method for the dataset.
    @property
    def data(self):
        return self._data

    # Step 3d: Create a method to describe a specific column in the dataset.
    def describe_column(self, column_name):
        if column_name in self._data.columns:
            return self._data[column_name].describe()
        else:
            return "Column not found"

    # Step 3e: Create a method to calculate the correlation between two columns.
    def correlation(self, column1, column2):
        if column1 in self._data.columns and column2 in self._data.columns:
            return self._data[[column1, column2]].corr()
        else:
            return "One or both columns not found"

    # Step 3f: Create a method to perform a simple linear regression analysis.
    def simple_regression(self, predictor, response):
        if predictor in self._data.columns and response in self._data.columns:
            from sklearn.linear_model import LinearRegression

            # Dropping rows with NaN values in the specified columns
            clean_data = self._data.dropna(subset=[predictor, response])

            X = clean_data[[predictor]].values.reshape(-1, 1)
            y = clean_data[response].values

            model = LinearRegression().fit(X, y)
            return model.coef_[0], model.intercept_
        else:
            return "One or both columns not found"

# Step 2: Demonstration of class functionality.
if __name__ == "__main__":
    # URL for the dataset
    dataset_url = "https://www.kaggle.com/datasets/fatihilhan/electric-vehicle-specifications-and-prices/data"

    # Step 3g: Create an instance of EVData with all required parameters.
    ev_data = EVData("EV_cars", "/Users/juanhuerta/Desktop/INFS3325/EV_cars.csv", dataset_url)

    # Step 3h: Load data from the specified path.
    ev_data.load_data()

    # Step 3i: Display meta-information.
    print(f"Dataset Name: {ev_data.dataset_name}")
    print(f"Dataset URL: {ev_data.dataset_url}")
    print(f"Number of Rows: {ev_data.num_rows}")
    print(f"Number of Columns: {ev_data.num_columns}")

    # Step 3j: Run descriptive statistics on a column.
    print(ev_data.describe_column("Range"))

    # Step 3k: Run correlation between two columns.
    print(ev_data.correlation("Range", "Price.DE."))

    # Step 3l: Run simple linear regression analysis.
    coef, intercept = ev_data.simple_regression("Range", "Price.DE.")
    print(f"Regression Coefficient: {coef}, Intercept: {intercept}")