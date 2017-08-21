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

	global positive_count
	global neutral_count
	global negative_count

	positive_count = 0
	neutral_count = 0
	negative_count = 0	

	for tweet in public_tweets:

		tweet_collection = {}
		
		
		polarity = TextBlob(tweet.text).sentiment.polarity

		
		tweet_collection['username'] = tweet.user.screen_name
		tweet_collection['tweet'] = tweet.text
		tweet_collection['polarity'] = polarity

		
		if polarity > 0:
			tweet_collection['color'] = 'green'
			tweet_collection['sentiment'] = 'positive'
			positive_count += 1

		elif polarity < 0:
			tweet_collection['color'] = 'red'
			tweet_collection['sentiment'] = 'negative'
			negative_count += 1
		else:
			tweet_collection['color'] = 'blue'
			tweet_collection['sentiment'] = 'neutral'
			neutral_count += 1


		all_tweets.append(tweet_collection)

	return all_tweets


def percent_calc():
	count = {}

	total_tweets = positive_count + neutral_count + negative_count

	if max(positive_count,negative_count) == positive_count:
		count['max'] = 'Positive'
	elif max(positive_count,negative_count) == negative_count:
		count['max'] = 'Negative'
	else:
		count['max'] = 'Balanced'

	percent_positive = (float(positive_count)/float(total_tweets)) * 100
	percent_neutral = (float(neutral_count)/float(total_tweets)) * 100
	percent_negative = (float(negative_count)/float(total_tweets)) * 100

	count['positive'] = "%.2f" % percent_positive 
	count['neutral'] = "%.2f" % percent_neutral
	count['negative'] = "%.2f" % percent_negative

	return count

























