# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 00:14:25 2021

@author: 44752
"""

from nltk.tokenize import word_tokenize

from nltk.corpus import stopwords

from nltk.sentiment.vader import SentimentIntensityAnalyzer


import string
import matplotlib.pyplot as plt
from collections import Counter


text=open(r"C:\Users\44752\Desktop\speech.txt").read()

text=text.lower()

text=text.replace("\n","")

text=text.translate(str.maketrans("","",string.punctuation))

tokenize_words=word_tokenize(text)

clean_words=[]

for i in tokenize_words:

    if i not in stopwords.words("english"):
        clean_words.append(i)

emotions=[]
with open(r"C:\Users\44752\Desktop\emotion.txt","r") as file:
    for i in file:

        text1=i.replace("\n","")
        text1=text1.strip()
        text1=text1.replace(" ","")
        text1=text1.replace(",","")
        text1=text1.replace("'","")

        word,emotion=text1.split(":")

        if word in clean_words:
            emotions.append(emotion)


def sentimentanalysis(text):
    return SentimentIntensityAnalyzer().polarity_scores(text)
sentiments=sentimentanalysis(text)
emotions_counter=Counter(emotions)
print(emotions_counter)
print(sentiments)
fig1,ax1=plt.subplots()
ax1.bar(emotions_counter.keys(),emotions_counter.values())
fig1.autofmt_xdate()
fig2,ax2=plt.subplots()
ax2.bar(sentiments.keys(),sentiments.values())
fig2.autofmt_xdate()
plt.show()