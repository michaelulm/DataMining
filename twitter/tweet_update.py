import twitter, json

# load config
from twitter_config import *

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

# update your current status
status_text = "Tweet tweet tweet :) !"
twitter_api.statuses.update(status=status_text)