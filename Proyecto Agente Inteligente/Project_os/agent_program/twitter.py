import tweepy
from pattern.web import Twitter
import time
import pprint
import webbrowser as wb

keys = dict(
    consumer_key =          'Xwn8UHCYuSBJr5iqmSk55YGysK',
    consumer_secret =       'UCbyb8beWpiNFPUsG4Dh4pt39h8Y97LGxor8w82XJiU8Ud21Ft',
    access_token =          '4475782283-DKs0tUCcxdpJLFciUUW7CBf5uqYufhKI0h3SZ7p',
    access_token_secret =   'Z3PDjdYNKbPbmQ3qAU5ntsJtlrnnY3Tocgf0RpHgVX0O8',
)

CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']
 
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

def post_tweet(users, message):
	for u in users:
	    message = message.rstrip()
	    m =  u + " " + message 
	    s = api.update_status(m)
	    time.sleep(3)


def read_tweet(is_mention):
	if is_mention:
		mentions = api.mentions_timeline()
		last_mention = mentions[0]
		print last_mention.text
		return last_mention.text
			
def get_tweet(keyword):
	max_tweets = 10
	searched_tweets = [status for status in tweepy.Cursor(api.search, q=keyword).items(max_tweets)]
	for s in searched_tweets:
		print s.text
    	print 

def get_trends(location):
	if location == 'local':
		trends = api.trends_place('23424919') # PERU WOEID 

	if location == 'global':
		trends = api.trends_place('1') # GLOBAL WOEID

	trends = set([trend['name'] for trend in trends[0]['trends']])
	for t in trends:
		print t.encode('utf8')
	
		
