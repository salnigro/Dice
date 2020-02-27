import random
from Deck import Deck

class Shuffler():
    
    def __init__(self,decks):
        self.deckt = []
        self.decks = decks
        self.combine()
        self.shuffle()
        
    def __str__(self):
        return ', '.join(str(card) for card in self.deckt)
  
    def combine(self):
        for i in range(0,len(self.decks)):
            for j in range(0,52):
                self.deckt.append(self.decks[i].index(j))
                
                
    def shuffle(self):
        n = len(self.deckt)
        for i in range(n-1,0,-1): 
            j = random.randint(0,i+1) 
            self.deckt[i],self.deckt[j] = self.deckt[j],self.deckt[i]

    def deal(self):
        return self.deckt.pop(0)
        
    def addcards(self,st):
        self.deckt.append(st)
        self.shuffle()
        
    def addDeck(self,deck):
        self.decks.append(deck)
        self.combine()
        self.shuffle()

    
