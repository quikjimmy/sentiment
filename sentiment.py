#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 20:28:34 2019

@author: jimmy
"""

import tweepy
from textblob import TextBlob
import pandas as pd
import matplotlib.pyplot as plt
import plotly.plotly as py
import numpy as np
from scipy.stats import shapiro

consumer_key = 'R23oMnOniJcPrtX60ZJXy4GeT'
consumer_secret = 'pQpJTEbVcegSs6HJ1HP8UHoMbACYGWBTLnS3EIn4Srhp1m1aFz'

access_token = '111690521-vj76ZLQ3xcNho0L43kSDR1M3VWx5x2sl7Yd6wEyv'
access_token_secret = 'HzhVk5Hq2y8eiLXuEDY6cC4HPnevvSfPPHkECdoTbwfOd'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

search_txt = 'spy'
wiki_txt = 'Six Sigma (6σ) is a set of techniques and tools for process improvement. It was introduced by engineer Bill Smith while working at Motorola in 1980.[1][2] Jack Welch made it central to his business strategy at General Electric in 1995. A six sigma process is one in which 99.99966% of all opportunities to produce some feature of a part are statistically expected to be free of defects.Six Sigma strategies seek to improve the quality of the output of a process by identifying and removing the causes of defects and minimizing variability in manufacturing and business processes. It uses a set of quality management methods, mainly empirical, statistical methods, and creates a special infrastructure of people within the organization who are experts in these methods. Each Six Sigma project carried out within an organization follows a defined sequence of steps and has specific value targets, for example: reduce process cycle time, reduce pollution, reduce costs, increase customer satisfaction, and increase profits.The term Six Sigma (capitalized because it was written that way when registered as a Motorola trademark on December 28, 1993) originated from terminology associated with statistical modeling of manufacturing processes. The maturity of a manufacturing process can be described by a sigma rating indicating its yield or the percentage of defect-free products it creates—specifically, within how many standard deviations of a normal distribution the fraction of defect-free outcomes corresponds to. Motorola set a goal of "six sigma" for all of its manufacturing.'

public_tweets = api.search(q=search_txt, count=1000)

twit_list = []
labels = ['sentiment_polarity']

for tweet in public_tweets:
    '''print(tweet.text)'''
    analysis = round(float(TextBlob(tweet.text).sentiment.polarity),3)
    #analysis = round(float(TextBlob(wiki_txt.text).sentiment.polarity),3)
    '''print(analysis.sentiment.polarity)'''
    twit_list.append(analysis)
    
df = pd.DataFrame(twit_list, columns=['Sentiment'])

print(df.describe())

#plt.hist(df)
plt.hist(df['Sentiment'])

# normality test
print('Mean: ', np.mean(df['Sentiment']))
stat, p = shapiro(df['Sentiment'])
print('Statistics=%.3f, p=%.5f' % (stat, p))
# interpret
alpha = 0.05

if p > alpha:
    print('Sample looks Gaussian (fail to reject H0)')
else:
    print ('Sample does not look Guassian (Reject H0)')
