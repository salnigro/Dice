from Deck import Deck

class Shuffler():
    
    def __init__(self,decks):
        self.decks = decks
  
    def combine(self):
        deck = []
        for i in range(0,len(self.decks)):
            for j in range(0,52):
                deck.append(self.decks[i].index(j))
        return deck
    
