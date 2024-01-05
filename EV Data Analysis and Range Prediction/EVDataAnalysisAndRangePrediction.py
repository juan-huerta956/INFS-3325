#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 11:29:22 2023

@author: juanhuerta
"""

"""
Purpose: This program analyzes an electric vehicle (EV) dataset, focusing on descriptive statistics, correlations, 
         and a simple regression model to predict the range based on battery size.
Inputs: EV dataset in CSV format.
Processing: 
    - Calculates descriptive statistics for numeric columns.
    - Computes correlation matrix for numeric columns.
    - Creates a simple regression model (battery size to predict range).
Outputs: 
    - Printed descriptive statistics.
    - Printed correlation matrix.
    - Summary of the regression model.
"""

# Importing necessary libraries
import pandas as pd
import statsmodels.api as sm

# Function to generate descriptive statistics
def descriptive_statistics(df):
    """Calculates and prints descriptive statistics for numeric columns in the dataset."""
    print("Function descriptive_statistics has started")

    # Selecting numeric columns for descriptive statistics
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    desc_stats = df[numeric_cols].describe()

    # Nested function to format results
    def format_results(stats):
        print("\nDescriptive Statistics:\n")
        print(stats)

    # Call the nested function with descriptive statistics
    format_results(desc_stats)

    return desc_stats

# Function to calculate correlations
def calculate_correlations(df):
    """Calculates and prints the correlation matrix for numeric columns in the dataset."""
    print("Function calculate_correlations has started")

    # Selecting numeric columns for correlation
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    correlations = df[numeric_cols].corr()

    # Nested function to format results
    def format_results(corr):
        print("\nCorrelation Matrix:\n")
        print(corr)

    # Call the nested function with the correlation matrix
    format_results(correlations)

    return correlations

# Function to create a simple regression model
def simple_regression_model(df):
    """Creates and prints a simple regression model using 'Battery' as predictor for 'Range'."""
    print("Function simple_regression_model has started")

    # Selecting the predictor and response variables
    X = df[['Battery']]  # Predictor variable
    y = df['Range']      # Response variable

    # Adding a constant to the predictor variable
    X = sm.add_constant(X)

    # Building the regression model
    model = sm.OLS(y, X).fit()

    # Nested function to format and display results
    def display_results(model):
        print("\nRegression Model Summary:\n")
        print(model.summary())

    # Call the nested function with the model results
    display_results(model)

    return model

# Main function
def main():
    """Main function to load the dataset and call analysis functions."""
    # Load the dataset
    df = pd.read_csv('/Users/juanhuerta/Desktop/INFS3325/EV_cars.csv')
    
    # Call functions to perform analysis
    print("Calling descriptive_statistics function")
    descriptive_stats = descriptive_statistics(df)

    print("Calling calculate_correlations function")
    correlations = calculate_correlations(df)

    print("Calling simple_regression_model function")
    regression_model = simple_regression_model(df)

    # Using the results
    # print(descriptive_stats, correlations, regression_model.summary())

# Program entry point
if __name__ == "__main__":
    main()
