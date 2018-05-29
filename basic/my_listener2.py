import sqlite3
import tweepy
import json
# import sqlite3 as db
# import pandas as pd
from tweet import Tweet
from tweet_user import Tweet_User
from user import User


class MyListener(tweepy.StreamListener):
    # def __init__(self, conn):
    #     self.conn = sqlite3.connect('twitter.db')
    #     self.c = self.conn.cursor()

    def create_connection(self):
        self.conn = sqlite3.connect('/Users/shruti/dev/python_skeleton/db_script/twitter.db')
        self.c = self.conn.cursor()

    def on_error(self, status):
        print('error is')
        print(status)
        if status == 420:
            return False

    def on_status(self, status):
        print('incoming')
        # if status.retweeted:
        #     print("------------------------------")
        #     print('retweeted')
        #     print("------------------------------")
        #     print(status)
        #     return

        # description = status.user.description
        # loc = status.user.location
        # text = status.text
        # coords = status.coordinates
        # geo = status.geo
        # name = status.user.screen_name
        # user_created = status.user.created_at
        # followers = status.user.followers_count
        # id_str = status.id_str
        # created = status.created_at
        # retweets = status.retweet_count
        # bg_color = status.user.profile_background_color

        tweet = json.loads(json.dumps(status._json))
        print("------------------------------")
        print(tweet)
        self.insert_data(tweet)
        print("------------------------------")

    def insert_data(self, tweet):
        try:
            print('Inside insert_data')
            tweet_id = self.insert_tweet_data(tweet)
            user_id = self.insert_user_data(tweet)
            self.insert_tweet_user_data(tweet_id, user_id)
            print("Committing :: ")
            self.conn.commit()
        except Exception as e:
            print('Exception occured while inserting records in db :: %s' % e)
            self.conn.rollback()

    def insert_tweet_data(self, tweet):
        t = Tweet(tweet['id'], tweet['created_at'], tweet['text'], tweet.get('source') or '')
        return t.insert_tweet(self.c)

    def insert_user_data(self, tweet):
        user = tweet.get('user')
        if user:
            u = User(user['id'], user['name'], user.get('description') or '', user.get('followers_count') or 0, user.get('statuses_count') or 0)
            return u.insert_user(self.c)

    def insert_tweet_user_data(self, tweet_id, user_id):
        #t = Tweet(tweet['id'], tweet['created_at'], tweet['text'], tweet.get('source') or '')
        tu = Tweet_User(tweet_id, user_id)
        tu.insert_tweet_user(self.c)

    def connection_close(self):
        self.conn.close()

    #     data = pd.read_json(tweet)
    #     columnsTitles = ['id', 'userId', 'title', 'body']
    #     data = data.reindex(columns=columnsTitles)
    #
    # #https://github.com/parroty/extwitter/issues/4
    #
    #
    #
    # # def on_data(self, data):
    # #     print('ondata::')
    # #     print(data)
    # def insertTweet(self):
    #
    #     c.execute("INSERT INTO tweets (tweetText, user, followers, date, location) VALUES (?, ?, ?, ?, ?)",
    #         (self.text, self.user, self.followers, self.date, self.location))
    #     conn.commit()
