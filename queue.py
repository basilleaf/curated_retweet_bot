import tweepy
import json
import redis
from flask import Flask
from auth import requires_auth
from config import queue_max_rows
from secrets import consumer_key, consumer_secret, access_token, access_token_secret

app = Flask(__name__)
rs = redis.Redis("localhost")

@app.route('/queue/<tweet_id>')
@requires_auth
def queue_tweet(tweet_id):
    """ endpoint takes tweet_id in url and save to redis queue """

    try:
        all_tweets = json.loads(rs.get('tweets'))
    except TypeError: 
        all_tweets = []

    tweet_id = int(tweet_id)
    if tweet_id not in [i['tweet_id'] for i in all_tweets]:

        tweet_meta = {
            'tweet_id':tweet_id, 
            'published':None
        }

        all_tweets.insert(0, tweet_meta)  # prepend
        rs.set('tweets', json.dumps(all_tweets[0:queue_max_rows]))

        return "Tweet Queued!"

    else:
        return "This tweet is already queued!"


if __name__ == '__main__':
    app.debug = True
    app.run()