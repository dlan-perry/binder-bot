




class decklist:

    def __init__(self, mainboard: list[dict], sideboard: list[dict]):
        self.mainboard = mainboard
        self.sideboard = sideboard
        self.name = "test"
        self.format = "test"
        self.author = "test"
        pass
    
    

    def to_mongo(self) -> dict:
        deck = {
            "name" : self.name,
            "format": self.format,
            "author": self.author,
            "main_deck" : self.mainboard,
            "sideboard" : self.sideboard
        }
        
        return deck

    @classmethod
    def load(input:dict):

        #returns the class from the DB return document
        pass

    def get_price(self):
        pass
    
    