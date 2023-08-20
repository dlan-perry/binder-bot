
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


def find_all_card_versions(card_name):
    res = db.cards.find({"name" : card_name, "lang": "en"})
    sets = set()
    for i in res:
        print(sets.add(i['set_name']))
    return sets



def find_decks(token:str):
    print("herrrr")
    #return decks.count_documents({"user_id": token}), decks.find({"user_id": token})
    pass

def add_deck(user_id: str, file):
    print(file)
    print(http.request("GET", file.url))
    print(http.request("GET", file.url).data.decode('utf-8').split("\r\n"))
    print(type(http.request("GET", file.url).data.decode('utf-8')))
    
    decklist = [{}, {}]    
    cards =  http.request("GET", file.url).data.decode("utf-8").split('\r\n')
    is_sideboard = 0
    for line in cards:
        if line != "":
            quantity, card_name = line.split(" ", 1)
            quantity = int(quantity)
            if find_card_by_name(card_name):
                decklist[is_sideboard][card_name] = quantity
        else:
            is_sideboard = 1
            print("\n****************\nSideboard Cards\n****************")


        '''
        if find_card_by_name(card_name):
            decklist[is_sideboard][card_name] = quantity
        '''
                          

    print(decklist[0])
    print(decklist[1])
    


            
    users.update_one({"user_id": user_id}, {'$push': {"decks" : {
                                                                "deck_name" : "test", 
                                                                "format": "modern",
                                                                "author": user_id,
                                                                "main_deck": decklist[0],
                                                                "sideboard": decklist[1]

                                                                }}})
    


def find_card_by_name(card_name: str):
    return cards.find_one({"name": card_name})

  