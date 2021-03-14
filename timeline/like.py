import os
import textwrap
import tweepy
from datetime import date, timedelta
from credentials import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
user = api.me()

# Bot Like Timeline
print(30 * '-')
print('[] Bot Like Timeline []')
print(30 * '-')
inuser = input(' Input username target : ')
jumlah = int(input(' Masukkan jumlah twit : '))

for status in tweepy.Cursor(api.user_timeline, screen_name=inuser).items(jumlah):
    try:
        print(30 * '=')
        print('\n[*] Tweet by: @' + status.user.screen_name)
        werap = textwrap.shorten(status.text, width=50)
        print(werap)
        print(status.created_at)
        print(status.source)
        api.create_favorite(status.id)
        print('Done !!!')
        print(30 * '=')
        print('\n')

    except tweepy.TweepError as e:
        print(e.reason)

    except StopIteration:
        break