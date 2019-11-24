#! python
# bot.py - the program which tweet the stuff.

import tweepy
from config import create_api
import time
import json

#Authentificate the session
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

#Load trees container file
with open ('csvjson.json', 'r') as file :
    data = file.read()

#Generate text for tweet
def get_spec(spec):
    return "Arbre 🌳 de #CIV225 #{}/465 \nL'arbre du jour est le {}. \nSon Appelation latine est {}. \
        \nLikez, retweetez, ajoutez photos & co en commentaires!\
        \n#deforestation #eauxetforets #forets #JePlanteMonArbreCI #reboisement #BringBackOurTrees".format(spec['ID'],
        spec['localName'], spec['latinName'])

def main():
    api = create_api()
    specList = json.loads(data)
    INTERVAL = 5
    for obj in specList :
        print('About to get tree')
        tree = get_spec(obj)
        api.update_status(tree)
        print("Waiting...")
        time.sleep(INTERVAL)

if __name__ == "__main__":
    main()