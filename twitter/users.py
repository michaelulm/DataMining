import twitter, json

# load config
from twitter_config import *

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

# query for users
results = twitter_api.users.search(q = '"Mike Ulm"')

# https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/user-object.html
# loop through each user, and print their details
for user in results:
	print("@%s (%s): %s" % (user["screen_name"], user["name"], user["location"]))
	print json.dumps(user, indent=1)
