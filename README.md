# SentimentAnalysis-with-twitter

App that can search for tweets based on a desired topic or person. User can view analysed tweets as positive, negative or neutral, along with relevant polarities. User can download csv version of tweets and sentiments.

View the app live at: [https://sentiment-analysis-twitter.herokuapp.com/](https://sentiment-analysis-twitter.herokuapp.com/)

[![](http://i.imgur.com/jRC0KkR.jpg)](https://{http://imgur.com/jRC0KkR})

## Development Guide

1. Create a virtualenv. `virtualenv somename`
2. cd into somename/
3. Activate the virtualenv. `source bin/activate`
4. cd into src/
5. Install the requirements. `pip install -r requirements.txt`
6. Make sure to enter the `ACCESS_TOKEN`, `ACCESS_TOKEN_SECRET`, `CONSUMER_KEY`, `CONSUMER_SECRET` variables in the views.py file inside search/.
7. Run the server as localhost. `python manage.py runserver`


