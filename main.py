#!/usr/bin/env python
# encoding: utf-8
#
# hUEY
# twitter scraping markov generator

import markovGenerator as MG
from time import sleep
import tweepy 
import csv
import random

#Turns out we need these keys locally, otherwise Tweepy doesn't quite work.
#The following method is copies from twitterScraper.py, see there for documentation.

#Twitter API credentials
#Fill these in!
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""

def get_all_tweets(screen_name):

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    alltweets = []  
    new_tweets = api.user_timeline(screen_name = screen_name,count=200,tweet_mode ='extended')
    alltweets.extend(new_tweets)
    oldest = alltweets[-1].id - 1

    while len(new_tweets) > 0 and len(alltweets) < 100:
        print ("getting tweets before %s" % (oldest))
        new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest,tweet_mode='extended')
        alltweets.extend(new_tweets)
        oldest = alltweets[-1].id - 1
        print ("...%s tweets downloaded so far" % (len(alltweets)))
        
    outtweets = [tweet.full_text for tweet in alltweets]
    with open('%s_tweets.txt' % screen_name,'w+') as f:
        for item in outtweets:
            f.write("%s\n" % item)
        f.close()
    pass





def main():
    # Interactive program that combines twitter scraping and markov generation
    # for easy user navigation! Hope you enjoy!
    #

    print("Hey there! We are going to generate text via a Markov Chain algorithm!")
    print("Do you want to use a local .txt file or scrape a twitter page? Type 'local' or 'twitter': ")
    mode = input("     > ")


    # local file case
    if mode == 'local':

        print()  
        print("Awesome! Type in the full name of the please, with extension. Remember, the file must be in the same folder!")
        print("Default files include (Shakespeare's) sonnets.txt!")
        fileName = input("     > ")
        print()

        # create the dictionary
        d = MG.createDictionary(fileName)

        while True: 
            print("How many words do you want me to generate?")
            l = input("     > ")
            print()

            outputlength = int(l)
            text = MG.generateText(d,outputlength)
            print(text)

            print()
            print("Hope you enjoyed!! Want some more? 'Y' or 'N'")
            yn = input("     > ")
            print()

            if yn == 'N':
                print("See you next time!")
                break

            elif yn == 'Y':
                continue

            else:
                print("I don't recognize that command!")

    elif mode == "twitter":

        print()  
        print("Great! Are the twitter access tokens set at the top of the file?")
        print("If you don't know what this means, or don't have any, contact Huey!")
        print("To exit, type 'quit'. Otherwise, any key will continue!")
        q = input("     > ")

        if q == 'quit':
            return 

        print()
        print("Sweet! Type in the full public twitter handle, without the '@'")
        print("For example, try 'realDonaldTrump':")
        handle = input("     > ")

        # create the .txt file
        get_all_tweets(handle)
        fileName = handle + "_tweets.txt"

        print()
        print("Got it! All their recent tweets have been written to file.")
        print("Creating Dictionary...")
        # I have a tendency for drama
        # You can wait a second :P
        sleep(0.3)
        print(".")
        sleep(0.3)
        print(".")
        sleep(0.3)
        print(".")
        sleep(0.3)
        print()
        # create the dictionary
        d = MG.createDictionary(fileName)

        while True: 
            print("Here's a generated tweet!")
            print()

            l = random.randrange(50,70)
            text = MG.generateText(d,l)

            #fixing up the endings!
            text = text[::-1]
            counter = 0
            for c in text:
                if c in '?.!':
                    break
                counter += 1
            
            text = text[counter:]
            text = text[::-1]
            print(text)

            print()
            print("Hope you enjoyed!! Want some more? 'Y' or 'N'")
            yn = input("     > ")
            print()

            if yn == 'N':
                print("See you next time!")
                break

            elif yn == 'Y':
                continue

            else:
                print("I don't recognize that command!")


if __name__ == "__main__":
    main()