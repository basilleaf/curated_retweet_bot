# Fav Retweet Bot

A python script that will retweet something you have recently favorited. In use with <a href = "https://twitter.com/hellohiking">@hellohiking</a>

## Install

### Install the script in a virtualenv


	  git clone https://github.com/basilleaf/fav_retweet_bot.git
	  cd fav_retweet_bot
	  virtualenv venv --distribute
	  source venv/bin/activate
	  pip install -r requirements.txt

### Setup your twitter creds

	• [authorize your app with twitter](https://apps.twitter.com/)

	• copy the file secrets_template.py to secrets.py and fill out your [twitter credentials](url)


## Usage

Visit Twitter and favorite things! Be logged in as the user who will be doing the retweeting and favoriting. Then run this script to retweet one recent fav:

	python retweet.py

To retweet regularly on a schedule you can use a [cron job](http://www.thegeekstuff.com/2009/06/15-practical-crontab-examples/).

Example crontab for retweeting once every 2 hours:

    0	*/2	*	*	*	<FULL PATH TO RETWEET BOT>/venv/bin/python <FULL PATH TO RETWEET BOT>retweet.py
