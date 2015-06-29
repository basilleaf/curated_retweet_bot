import tweepy
import json
import redis 
import random
from auth import requires_auth
from time import strftime
from config import queue_max_rows
from secrets import consumer_key, consumer_secret, access_token, access_token_secret

rs = redis.Redis("localhost")

def get_next_tweet():
    """ get next tweet in queue, returns twitter tweet id """
    try:
        all_tweets = json.loads(rs.get('tweets'))
    except TypeError: 
        all_tweets = []

    tweet_id = random.choice([i['tweet_id'] for i in all_tweets if not i['published']])
    return tweet_id


def retweet(tweet_id):
    """ retweet the tweet_id """

    tweet_id = int(tweet_id)

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    retweeted = True
    try:
        api.retweet(id=tweet_id)
    except tweepy.error.TweepError:
        print tweepy.error.TweepError.__str__
        retweeted = False

    mark_as_retweeted(tweet_id, retweeted)

    if not retweeted:
        print "unable to tweet, marked published=error"
    else:
        print "ok %s" % tweet_id


def mark_as_retweeted(tweet_id, retweeted):
    """ updates the tweet's published field """
    # now set its published date and update the database
    try:
        all_tweets = json.loads(rs.get('tweets'))
    except TypeError: 
        all_tweets = []

    index = [i['tweet_id'] for i in all_tweets].index(tweet_id)
    all_tweets[index]['published'] = strftime("%Y-%m-%d %H:%M:%S")
    if not retweeted:
        all_tweets[index]['published'] = 'error'
    rs.set('tweets', json.dumps(all_tweets[0:queue_max_rows]))


if __name__ == '__main__':
    tweet_id = get_next_tweet()
    retweet(tweet_id)