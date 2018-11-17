import twitter, json

# load config
from twitter_config import *

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

tweet_id = 1059059980530339840

# get single tweet
tweet = twitter_api.statuses.show(id=tweet_id)
# simple output loaded tweet
print(json.dumps(tweet, indent=1))
