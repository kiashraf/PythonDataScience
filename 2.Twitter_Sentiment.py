# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 17:47:21 2018

@author: Khalid
"""
import tweepy

from textblob import TextBlob

consumer_key ='3NGDOGmLqktH1kb8N59xfNWmv'

consumer_secret= '65z9aVcO7ad8cqY0tEDSuRCbknWgrHFkY1MShl3lmziNEI8bwe'

access_token = '1610112967-MwIfyI6MuHQtQmj0nF2tIPYTrrB6H5otTqFgret'
access_token_secret='DNxOIVCBdKf7iAyvDVHwIYh41fut4npXMuDAKS9hEZsAq'


auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)


api = tweepy.API(auth)

public_tweets = api.search('Modi',count=100)

import csv

with open('Modi_sentiment.csv','w',newline='',encoding='utf-8') as file:
    writer = csv.writer(file)
    for tweet in public_tweets:
        analysis = TextBlob(tweet.text)
        polarity = 'positive' if analysis.sentiment[0]>=0 else 'negative'
        writer.writerow([tweet.text+ " : " +polarity])  
        