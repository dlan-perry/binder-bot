
from pymongo import MongoClient
import urllib3

http = urllib3.PoolManager()
client = MongoClient("localhost", 27017, maxPoolSize=50)
db = client.tradability
cards = db['cards']
users = db['users']
decks = db['decks']
cursor = cards.find({"name": "Static Orb"})



def add_user(token:str):
    if not users.find_one({"user_id": token}):
        users.insert_one({"user_id" : token})
        return True
    else:
        print("user already exists")
        return False

def find_decks(token:str):
    print("herrrr")
    return decks.count_documents({"user_id": token}), decks.find({"user_id": token})
    pass

def add_deck(user_id: str, file):
    decklist = []
    for line in http.request("GET", file.url).data:
        if line != "":
            decklist.append(str(line))
    decks.insert_one({"user_id": user_id,
                      "cards": decklist})


def find_card_by_name(card_name: str):
    print(card_name)
    print(repr(card_name))
    return cards.find_one({"name": card_name})

