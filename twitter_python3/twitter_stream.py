import twitter, json, sys

from twitter_config import *

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

# Finding topics of interest by using the filtering capablities it offers.
# Query terms
q = 'Education' # Comma-separated list of terms

print('Filtering the public timeline for track="%s"' % (q,))

# Reference the self.auth parameter
twitter_stream = twitter.TwitterStream(auth=twitter_api.auth)

# See https://dev.twitter.com/docs/streaming-apis
stream = twitter_stream.statuses.filter(track=q)

for tweet in stream:
	print("---------------------------------------------------")
	print("Tweet: " + str(tweet['text'].encode('utf-8')))