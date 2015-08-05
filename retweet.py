import tweepy
from random import randint
from time import sleep
from secrets import consumer_key, consumer_secret, access_token, access_token_secret

base_path = '/users/lballard/projects/hellohiking/'
tweeted_file = base_path + 'tweeted.txt'


def get_previously_tweeted():
    """ gets list of previously tweeted from file """
    with open(tweeted_file) as f:
        tweeted = f.read().splitlines()

    return tweeted


def get_next_tweet(page=None):
    """ get next tweet in queue, returns twitter tweet id """
        
    if not page: page = 1

    tweeted = get_previously_tweeted()

    tweepy_favs = api.favorites(page=page)  # first page of favs = 20 favs
    tweepy_favs.reverse()

    for tweet_id in [f.id for f in tweepy_favs]:
        if str(tweet_id) not in tweeted:
            return tweet_id

    # if we are still here then we didn't find a tweet in the first page of favs
    # that has not already been tweeted, so go to next page
    page = page + 1
    return get_next_tweet(page=page)


def retweet(tweet_id):
    """ retweet the tweet_id """

    tweet_id = int(tweet_id)

    try:
        api.retweet(id=tweet_id)
        mark_as_retweeted(tweet_id)
        print "ok %s" % tweet_id
    except tweepy.error.TweepError:
        print tweepy.error.TweepError.__str__
            
    mark_as_retweeted(tweet_id)  # mark as retweeted either way


def mark_as_retweeted(tweet_id):
    """ writes the tweet id to the file """
    
    print 'wriing to file'
    with open (tweeted_file, 'a') as f: 
        f.write ("%i\n" % tweet_id)



if __name__ == '__main__':
    """
    this will be on something like hourly cron, 
    but we don't want to really tweet on the hour 
    or even at the same time every day
    so sleep for a random number of seconds between zero and 1 hour 
    """
    sleep_time = randint(0,3600)
    print "sleeping for %s" % sleep_time
    sleep(sleep_time)


    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    
    tweet_id = get_next_tweet()
    retweet(tweet_id)

