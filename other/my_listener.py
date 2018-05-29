# import tweepy
# import json
# # import sqlite3 as db
# # import pandas as pd
#
# class MyListener(tweepy.StreamListener):
#     def on_error(self, status):
#         print('error is')
#         print(status)
#         if status == 420:
#             return False
#     def on_status(self, status):
#         if status.retweeted:
#             print("------------------------------")
#             print('retweeted')
#             print("------------------------------")
#             print(status)
#             return
#
#         description = status.user.description
#         loc = status.user.location
#         text = status.text
#         coords = status.coordinates
#         geo = status.geo
#         name = status.user.screen_name
#         user_created = status.user.created_at
#         followers = status.user.followers_count
#         id_str = status.id_str
#         created = status.created_at
#         retweets = status.retweet_count
#         bg_color = status.user.profile_background_color
#
#         tweet = json.dumps(status._json)
#         print("------------------------------")
#         print(tweet)
#         print("------------------------------")
#     #     data = pd.read_json(tweet)
#     #     columnsTitles = ['id', 'userId', 'title', 'body']
#     #     data = data.reindex(columns=columnsTitles)
#     #
#     # #https://github.com/parroty/extwitter/issues/4
#     #
#     #
#     #
#     # # def on_data(self, data):
#     # #     print('ondata::')
#     # #     print(data)
