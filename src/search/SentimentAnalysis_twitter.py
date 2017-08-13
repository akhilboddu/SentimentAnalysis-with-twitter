import tweepy
import csv
from textblob import TextBlob

def authenticate(consumer_key, consumer_secret, access_token, access_token_secret):
	""" Authenticate tweets """
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	global api 
	api = tweepy.API(auth) 

def search_twitter(searchItem):
	""" Search using tweepy api """
	public_tweets = api.search(searchItem)
	return public_tweets

def classify_tweets(public_tweets):
	""" Classify tweets into an array """
	all_tweets = []
	for tweet in public_tweets:

		tweet_collection = {}

		polarity = TextBlob(tweet.text).sentiment.polarity

		tweet_collection['username'] = tweet.user.screen_name
		tweet_collection['tweet'] = tweet.text
		tweet_collection['polarity'] = polarity

		if polarity > 0:
			tweet_collection['color'] = 'green'
			tweet_collection['sentiment'] = 'positive'
		elif polarity < 0:
			tweet_collection['color'] = 'red'
			tweet_collection['sentiment'] = 'negative'
		else:
			tweet_collection['color'] = 'blue'
			tweet_collection['sentiment'] = 'neutral'


		all_tweets.append(tweet_collection)

	return all_tweets

