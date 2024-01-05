#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri July 5 01:36:24 2023

@author: juanhuerta
"""

## File path for your local machine
local_file_path = '/Users/juanhuerta/Desktop/INFS3325/miyamoto_mushashi.txt'

## Text Reader Object: Creating the file reader object
with open(local_file_path, 'r') as file:
    ## Create Text Variable: Reading the content of the file
    myQuote = file.read()
    
## Creating a variable for the intro label
myIntro = "Quote by Miyamoto Musashi: "

## Quote Output to Console
print(myIntro + '\n' + myQuote)
