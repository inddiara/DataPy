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

for tweet in tweepy.Cursor(api.search,
                           q=query,
                           rpp=100,
                           lang="pt").items(200):
	#print(tweet.text)
	# results.append(tweet.text)
    results = [[tweet.created_at, tweet.text]]

#print(len(results))
#
print(results)

outtweets = [[tweet.created_at, tweet.text] for item in results]

# with open('%s_tweets.csv', 'wb') as f:
#		writer = csv.writer(f)
#		writer.writerow(["id","created_at","text"])
#		writer.writerows(outtweets)

with open('results.csv', 'w') as f:
    writer = csv.writer(f)
    #for item in results:
    writer.writerow(["Data", "Tweet"])
    writer.writerows(results)


