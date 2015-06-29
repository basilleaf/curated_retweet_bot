work in progress.. 

This is a Flask app and browser extension combo that provides a way to browse tweets with images in twitter and curate a queue of the selected tweets to be retweeted later on a schedule. 

It has 2 parts: 

	- a chrome extension that adds a button to twitter's image gallery overlay in an image search results page 

	- a Flask app that does 2 things:

		- API endpoint accepts a twitter id and adds it to a redis queue

		- cron (or other scheduler) script that selects an unpublished tweet from the queue and retweets it


todo: make the chrome extension - where to put the tweet button:

<small class="time">

    ::before
    <a class="tweet-timestamp js-permalink js-nav js-tooltip" title="3:58 PM - 28 Jun 2015" href="/the_kizzle/status/615293286962466816"></a>

</small>


