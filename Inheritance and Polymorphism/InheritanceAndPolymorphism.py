#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 01:32:54 2023

@author: juanhuerta
"""

import pandas as pd

# Set Pandas options to display all columns
pd.set_option('display.max_columns', None)

# MARK/LABEL: Step 11a - parent class header
class CarWeightReport:  # Parent class
    # MARK/LABEL: Step 11b - parent class constructor
    def __init__(self, model_name):
        self.__carModel = model_name
        self.__carWt = None

    # MARK/LABEL: Step 11c - __carModel get method
    @property
    def carModel(self):
        return self.__carModel

    @property
    def carWt(self):
        return self.__carWt

    # MARK/LABEL: Step 11d - __carWt set method decorator
    @carWt.setter
    def carWt(self, weight):
        self.__carWt = weight

    @property
    def report(self):
        shortReport = f"The {self.carModel} weighs {self.carWt} pounds."
        return shortReport

# Child class
# MARK/LABEL: Step 11e - class inherited from
class SportcarReport(CarWeightReport):  # Child class inherits from CarWeightReport
    def __init__(self, model_name):
        # MARK/LABEL: Step 11f - call parent constructor
        super().__init__(model_name)
        self.__carHP = None

    @property
    def carHP(self):
        return self.__carHP

    @carHP.setter
    def carHP(self, horsepower):
        self.__carHP = horsepower

    # MARK/LABEL: Step 11g - Polymorphism in the child class
    @property
    def report(self):
        hp_wt_ratio = self.carWt / self.carHP
        longReport = f"The {self.carModel} weighs {self.carWt} pounds.\nHorsepower to weight ratio: {hp_wt_ratio:.2f}"
        return longReport

# Main body of the program
mtcars_DF = pd.read_csv('/Users/juanhuerta/Desktop/INFS3325/mtcars.csv')  # Adjust the file path if needed
print(mtcars_DF)

# Parent class object
f0 = CarWeightReport("Mazda RX4")
print(f0.carModel)

row_for_report = mtcars_DF[mtcars_DF['model'] == f0.carModel]
print("Row for report:", row_for_report)

nextWeight = row_for_report['wt'].iloc[0] * 1000
realWeight = int(nextWeight)
f0.carWt = realWeight

print(f0.report)

# Child class object
f1 = SportcarReport("Ferrari Dino")
row_for_report = mtcars_DF[mtcars_DF['model'] == f1.carModel]
print("Row for report:", row_for_report)

nextWeight = row_for_report['wt'].iloc[0] * 1000
realWeight = int(nextWeight)
f1.carWt = realWeight

f1.carHP = row_for_report['hp'].iloc[0]

print(f1.report)
