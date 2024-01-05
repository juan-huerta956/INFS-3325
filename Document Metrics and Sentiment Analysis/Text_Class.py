#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 10:07:09 2023

@author: juanhuerta
"""

from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.corpus import stopwords


class document_metrics:
    def __init__(self, documentName, fullText):
        # Initialize the protected variables using name mangling
        self.__documentName = documentName
        self.__fullText = fullText
        self.__wordCountAll = None
        self.__wordCountNoStopwords = None
        self.__documentPosSentiment = None
        self.__documentNegSentiment = None
        self.__documentCompoundSentiment = None

    @property
    def documentName(self):
        return self.__documentName
    
    @documentName.setter
    def documentName(self, documentName):
        self.__documentName = documentName

    @property
    def fullText(self):
        return self.__fullText
    
    @fullText.setter
    def fullText(self, fullText):
        self.__fullText = fullText

    @property
    def wordCountAll(self):
        return self.__wordCountAll
    
    @wordCountAll.setter
    def wordCountAll(self, value):
        self.__wordCountAll = value

    @property
    def wordCountNoStopwords(self):
        return self.__wordCountNoStopwords
    
    @wordCountNoStopwords.setter
    def wordCountNoStopwords(self, value):
        self.__wordCountNoStopwords = value

    @property
    def documentPosSentiment(self):
        return self.__documentPosSentiment
    
    @documentPosSentiment.setter
    def documentPosSentiment(self, value):
        self.__documentPosSentiment = value

    @property
    def documentNegSentiment(self):
        return self.__documentNegSentiment
    
    @documentNegSentiment.setter
    def documentNegSentiment(self, value):
        self.__documentNegSentiment = value

    @property
    def documentCompoundSentiment(self):
        return self.__documentCompoundSentiment

    @documentCompoundSentiment.setter
    def documentCompoundSentiment(self, value):
        self.__documentCompoundSentiment = value
        
with open('/Users/juanhuerta/Desktop/INFS3325/Oracle_Colombia_Cloud.txt', 'r', encoding='utf-8') as file0:
    myText = file0.read()
file0.close()

f0 = document_metrics("Oracle_Colombia_Cloud.txt", myText)

myTextWords = myText.split()
myCount = len(myTextWords)
f0.wordCountAll = myCount
print("\nYour document contains " + str(f0.wordCountAll) + " words")
f0.wordCountAll = myCount

myStopwords = set(stopwords.words('english'))
myTextWordsNON = [word for word in myTextWords if word.lower() not in myStopwords]

myCountNON = len(myTextWordsNON)
print("You have " + str(myCountNON) + " non-stopwords in your document")
f0.wordCountNoStopwords = myCountNON

sia = SentimentIntensityAnalyzer()
mySentimentMeasures = sia.polarity_scores(myText)
print(mySentimentMeasures)

f0.documentNegSentiment = mySentimentMeasures['neg']
f0.documentPosSentiment = mySentimentMeasures['pos']
f0.documentCompoundSentiment = mySentimentMeasures['compound']

print("\nDocument name: " + f0.documentName)
print("\nFull Text: " + f0.fullText)
print("\nWord Count All: " + str(f0.wordCountAll))
print("Word Count no Stopwords: " + str(f0.wordCountNoStopwords))
print("Negative Sentiment: " + str(f0.documentNegSentiment))
print("Positive Sentiment: " + str(f0.documentPosSentiment))
print("Compound Sentiment: " + str(f0.documentCompoundSentiment))
