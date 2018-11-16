import twitter, json

# load config
from twitter_config import *

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

# get your http://woeid.rosselliot.co.nz/
# tested valid https://codebeautify.org/jsonviewer/f83352
woe_id = 23424750	# austria
# loads current trends
results = twitter_api.trends.place(_id = woe_id)

# print json -> easier readable 
#print json.dumps(results, indent=1)

for trend in results[0]['trends']:
	print trend['name'] 
