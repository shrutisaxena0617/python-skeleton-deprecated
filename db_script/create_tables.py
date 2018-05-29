# get connection and cursor objects

import sqlite3

conn = sqlite3.connect('twitter.db')
c = conn.cursor()

try:
    # create tables
    c.execute('''create table tweets (
        id integer,
        created_at text,
        tweet_text text,
        source text
    )''')
    c.execute('''create table users (
        id integer,
        name text,
        description text,
        follower_count integer,
        statuses_count integer
    )''')
    c.execute('''create table tweet_user (
        tweet_id integer,
        user_id integer
    )''')
    conn.close()
except Exception as e:
    print("Exception occured while creating tables %s" % e)
    conn.close()