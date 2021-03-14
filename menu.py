import os
import tweepy
import sys
from credentials import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()
print ("""\
┏━━┓╋┏┳┓┏┓╋╋╋╋╋┏━━┓╋┏┓
┗┓┏╋┳╋┫┗┫┗┳━┳┳┓┃┏┓┣━┫┗┓
╋┃┃┃┃┃┃┏┫┏┫┻┫┏┛┃┏┓┃╋┃┏┫
╋┗┻━━┻┻━┻━┻━┻┛╋┗━━┻━┻━┛""")
print (30 * '=')
print (" Selamat Datang     " + user.name)    
print (" Lokasi Kamu di     " + user.location)
print (30 * '=')
print ("1. Bot Like (via search)")
print ("2. Bot Retweet (via search)")
print ("3. Bot Like dan Retweet (via search)")
print ("4. Bot Like Timeline")
print ("5. Bot Retweet Timeline")
print ("6. Bot Retweet dan Like Timeline")
print (30 * '-')
 
## Pilihan Menu ###
choice = input('Pilih angka [1-6] : ')
 
##
choice = int(choice)
 
###
if choice == 1:
        from search.like import *
elif choice == 2:
        from search.retweet import *
elif choice == 3:
        from search.lr import *
elif choice == 4:
        from timeline.like import *
elif choice == 5:
        from timeline.retweet import *
elif choice == 6:
        from timeline.lr import *
else:    ## default ##
        print ("Salah pencet, silahkan ulangi lagi...")