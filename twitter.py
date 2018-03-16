#!/usr/bin/env python
# encoding: utf-8

import tweepy #https://github.com/tweepy/tweepy
import csv

#Twitter API credentials
consumer_key = "eCdJHcgdrD5uoniX7STab8jKz"
consumer_secret = "Bfhw1h74brnqviHU7btT9HSGlLnMIJHq7VMbj1tiJSB5riK2WV"
access_key = "974020392552714241-NkMx5yQd2mee5ZM9PBBxdfYJxmHcBJJ"
access_secret = "YaDvoAuODEN89ZXJVMmKjN36cc9dVCw69LuxPhfXiyqCX"


# Creating the authentication object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# Setting your access token and secret
auth.set_access_token(access_key, access_secret)

# Creating the API object while passing in auth information
api = tweepy.API(auth)

# The search term you want to find
query = "pje"
# Language code (follows ISO 639-1 standards)
language = "pt"

results = []

# Open/create a file to append data to
csvFile = open('result.csv', 'w')

#Use csv writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,
                           q=query,
                           rpp=100,
                           lang="pt").items(200):
  # Write a row to the CSV file. I use encode UTF-8
    csvWriter.writerow([tweet.created_at, tweet.text])
    print ([tweet.created_at, tweet.text])
csvFile.close()



