# Class for defining a Tweet
class Tweet():

    # Data on the tweet
    def __init__(self, id, created_at, text, source):
        self.id = id
        self.created_at = created_at
        self.text = text
        self.source = source

    # Inserting that data into the DB
    def insert_tweet(self, c):

        try:

            c.execute('INSERT INTO tweets (id, created_at, tweet_text, source) VALUES (?, ?, ?, ?)',
                (self.id, self.created_at, self.text, self.source))
            return self.id
            #conn.commit()

        except Exception as e:
            print("Code fatifaying in insert_tweet %s" % e)
