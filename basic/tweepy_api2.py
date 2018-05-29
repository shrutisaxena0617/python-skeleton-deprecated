import tweepy
import pandas as pd
import requests
import json
import signal
import sys
import sqlite3

from my_listener2 import MyListener

TWITTER_KEY = '2693355300-SKXNm8qxdkfdQJzR3paNvbge3n1DaJRVaHgYDxD'
TWITTER_SECRET = 'N7tw0btVqVMvNkAgyDesIfJLn0CRk6HjLdKHGZ3ymY6lU'
TWITTER_APP_KEY = 'PGouZB8NYgIjCo3uEM5URhMRH'
TWITTER_APP_SECRET = 'DAAbhNzrF7qSxsJIkxhCQGjELOx6MrXXuZXVeGGsTu74TrLVhe'

# Creating tweets table in twitter.db database using sqlite3

# def signal_handler(signal, frame):
#     print('Disconneting twitter_stream :: ')
#     twitter_stream.disconnect()
#     sys.exit(0)
auth = tweepy.OAuthHandler(TWITTER_APP_KEY, TWITTER_APP_SECRET)
auth.set_access_token(TWITTER_KEY, TWITTER_SECRET)

api = tweepy.API(auth)
mylistener = MyListener()
mylistener.create_connection()
try:
    # conn = sqlite3.connect('twitter.db')
    #c = conn.cursor()
    twitter_stream = tweepy.Stream(auth, mylistener)
    twitter_stream.filter(track=['avengersinfinitywar', 'deadpool2', 'cryptocurrency', 'Celtics', 'NBAFinals'], languages=["en"])
    # twitter_stream.filter(track=['cryptocurrency -filter:retweets', 'deadpool2 -filter:retweets', 'NBAFinals -filter:retweets'], languages=["en"])
except KeyboardInterrupt as e:
    print('Exception occured ::  %s' % e)
    print('Disconnecting twitter_stream :: ')
    twitter_stream.disconnect()
    mylistener.connection_close()
except Exception as e:
    print('Exception occured ::  %s' % e)
    print('Disconnecting twitter_stream :: ')
    twitter_stream.disconnect()
    mylistener.connection_close()
    # conn.close()


# signal.signal(signal.SIGINT, signal_handler)
# signal.pause()
