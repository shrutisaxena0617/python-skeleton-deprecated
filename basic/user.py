# Class for defining a Tweet
class User():

    # Data on the tweet
    def __init__(self, id, name, description = None, follower_count = 0, statuses_count = 0):
        self.id = id
        self.name = name
        self.description = description
        self.follower_count = follower_count
        self.statuses_count = statuses_count

    # Inserting that data into the DB
    def insert_user(self, c):

        try:

            c.execute("INSERT INTO users (id, name, description, follower_count, statuses_count) VALUES (?, ?, ?, ?, ?)",
                (self.id, self.name, self.description, self.follower_count, self.statuses_count))
            return self.id
            #conn.commit()

        except Exception as e:
            print("Code fatifaying in insert_user %s" % e)
