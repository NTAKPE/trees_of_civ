#! python
# bot.py - the program which tweet the stuff.

import tweepy
from config import create_api
import time
import json

#Load trees container file
with open ('csvjson.json', 'r') as file :
    data = file.read()

#Generate text for tweet
def get_spec(spec):
    return "🌳 Arbre #{}/465\nL'arbre du jour est le {} (nom latin :{}). \
        \nSource: Atlas Des Bois De Côte d'Ivoire Tome 1\
        \n#BringBackOurTrees #BoisDeCIV #CIV225".format(spec['ID'],
        spec['localName'], spec['latinName'])

def main():
    api = create_api()
    specList = json.loads(data)
    INTERVAL = 60*60*24
    for obj in specList :
        print('About to get tree')
        tree = get_spec(obj)
        api.update_status(tree)
        print("Waiting...")
        time.sleep(INTERVAL)

if __name__ == "__main__":
    main()