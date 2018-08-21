#!/usr/bin/env python
# encoding: utf-8
#
# hUEY
# twitter scraping

import tweepy #https://github.com/tweepy/tweepy
import csv

#Twitter API credentials
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""


def get_all_tweets(screen_name):

    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    #initialize a list to hold all the tweepy Tweets
    alltweets = []  

    #make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name = screen_name,count=200,tweet_mode ='extended')

    #save most recent tweets
    alltweets.extend(new_tweets)

    #save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1

    #keep grabbing tweets until you hit 300 or so
    while len(new_tweets) > 0 and len(alltweets) < 100:
        print ("getting tweets before %s" % (oldest))

        #all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest,tweet_mode='extended')

        #save most recent tweets
        alltweets.extend(new_tweets)

        #update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1

        print ("...%s tweets downloaded so far" % (len(alltweets)))


    #extract the text from each tweet to populate the .txt file
    outtweets = [tweet.full_text for tweet in alltweets]


    #write to file
    with open('%s_tweets.txt' % screen_name,'w+') as f:
        for item in outtweets:
            f.write("%s\n" % item)
        f.close()
    pass


if __name__ == '__main__':
    #pass in the username of the account you want to download
    get_all_tweets("realDonaldTrump")