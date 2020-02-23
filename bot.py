#! python
# bot.py - the program which tweet the stuff.

import tweepy
from config import create_api
from quotes import quotes
import time

def main():
    #Create twitter API
    api = create_api()

    #Set the loop parameters
    INTERVAL_TWO = 60*60*3

    while True:
        INTERVAL_ONE = 60*60*4
        quoteList = quotes()
        for quote in quoteList :
            api.update_status(quote)
            time.sleep(INTERVAL_ONE)
        time.sleep(INTERVAL_TWO)

if __name__ == "__main__":
    main()