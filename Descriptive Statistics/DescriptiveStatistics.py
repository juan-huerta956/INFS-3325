#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri July 5 12:36:24 2023

@author: juanhuerta
"""

import pandas as pd ## Load Pandas

file_path = '/Users/juanhuerta/Desktop/INFS3325/access_to_computers.csv'
computers_DF = pd.read_csv(file_path) ## Read CSV

print(type(computers_DF)) ## Dataframe Type

print(computers_DF.shape) ## Dataframe Header Names

print(computers_DF['Value'].describe()) ## Descriptives for Values Column