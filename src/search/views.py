# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .forms import SearchForm
from django.http import Http404
from django import forms 
from django.views import View
from django.core.files import File 
import os
from . import SentimentAnalysis_twitter
import tweepy
from textblob import TextBlob
import csv

consumer_key = "sHRxqSp3bNAnWJUkCbk6o5QId"
consumer_secret = "hgYO6QrQyoLuVLPdlRdaUMShB2WvmSSG9HSkoLmcZLLXK96Xr1"
access_token = "778157980864901122-XWS2Zirk9LEzf6aaP32yJGKZtWsZpQW"
access_token_secret = "EvdGivtun66bjAakTSHI0fdgCDlFuYvZhoPnulcMkoutT"

def index(request, *args, **kwargs):
	""" Home page """
	form = SearchForm()
	context = {
		'form': form,
	}
	return render(request, 'search/index.html', context)

def get_name(request):
	""" Page to be returned when the analyse button is triggered """
	if request.method == 'POST':
		form = SearchForm(request.POST)
		if form.is_valid():
			search = form.cleaned_data['search']
	else:
		form = SearchForm()

	SentimentAnalysis_twitter.authenticate(consumer_key, consumer_secret, access_token, access_token_secret)
	global public_tweets
	public_tweets = SentimentAnalysis_twitter.search_twitter(search)
	global all_tweets
	all_tweets = SentimentAnalysis_twitter.classify_tweets(public_tweets)
	percentage = SentimentAnalysis_twitter.percent_calc()
	
	context = {
		'search' : search,
		'all_tweets' : all_tweets,
		'percentage' : percentage,
	}

	return render(request, 'search/search-results.html', context)

def download_csv(request):
	""" When download button is triggered """

	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="analysis.csv"'

	fieldnames = ['Tweet', 'Sentiment']
	writer = csv.DictWriter(response, fieldnames=fieldnames)
	writer.writeheader()

	for d in all_tweets:
    
		writer.writerow({
				'Tweet' : d['tweet'].encode('ascii', 'ignore').decode('ascii'),
				'Sentiment' : 'Postive',
			})

	return response

	








