# Class for defining a Tweet
class Tweet_User():

    # Data on the tweet
    def __init__(self, tweet_id, user_id):
        self.tweet_id = tweet_id
        self.user_id = user_id

    # Inserting that data into the DB
    def insert_tweet_user(self, c):

        try:

            c.execute("INSERT INTO tweet_user (tweet_id, user_id) VALUES (?, ?)",
                (self.tweet_id, self.user_id))
        #conn.commit()

        except Exception as e:
            print("Code fatifaying in insert_tweet_user %s" % e)
