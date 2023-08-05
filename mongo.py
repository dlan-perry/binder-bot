
from pymongo import MongoClient
import urllib3

http = urllib3.PoolManager()
client = MongoClient("192.168.1.101", 27017, maxPoolSize=50)
db = client.binder_bot
cards = db['cards']
users = db['users']
cursor = cards.find({"name": "Static Orb"})

"""

Example Deck Structure
{"deck1": [
            {"format" : format},
            {"main_deck": [
            {"card_name": amount},
            {"card_name2": amount}
            ]}, 
            {"sideboard": []}
          ]
}

"""

def add_user(token:str):
    if not users.find_one({"user_id": token}):
        users.insert_one({
                          "user_id" : token,
                          "decks" : [],
                          "binders": {
                              "selling":[],
                              "trading":[], 
                              "looking":[], 
                              "have":[]
                            }
                          })
        return True
    else:
        print("user already exists")
        return False


def add_to_binder(user_id, card_name, set, binder="trading", quantity=1):
    db.users.update_one({"user_id": user_id}, {'$push' : {"binders." + binder : {"card_name" : "ponder"}} })
    pass





def find_decks(token:str):
    print("herrrr")
    #return decks.count_documents({"user_id": token}), decks.find({"user_id": token})
    pass

def add_deck(user_id: str, file):
    decklist = []
    for line in http.request("GET", file.url).data:
        if line != "":
            decklist.append(str(line))
    users.find_one({"user_id": user_id})["decks"].insert_one({"user_id": user_id,
                      "cards": decklist})


def find_card_by_name(card_name: str):
    print(card_name)
    print(repr(card_name))
    return cards.find_one({"name": card_name})

  