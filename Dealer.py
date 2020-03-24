from Player import Player
from Card import Card
from Deck import Deck
from Shuffler import Shuffler
class Dealer(object):
   
    
    def __init__(self,players,shuffler):
        self.cards = []
        self.players = players
        self.shuffler = shuffler
        

    def __str__(self):
        return ', '.join(str(card) for card in self.cards)
    
    def deal(self):
        for i in range(len(self.players)):
            self.players[i].cards.append(self.shuffler.deal())
        self.cards.append(self.shuffler.deal())
        for i in range(len(self.players)):
            self.players[i].cards.append(self.shuffler.deal())
        self.cards.append(self.shuffler.deal())
        
        for i in range(0,len(self.players)):
            print(str(self.players[i]))
            t = input("Player " + str(i+1) + " hit or stand. ") 
            while(t == "hit"):
                self.players[i].cards.append(self.shuffler.deal())
                print(str(self.players[i]))
                t = input("Player " + str(i+1) + " hit or stand. ")
        self.selfdeal()
        self.won()

    def selfdeal(self):
        print(str(self))
        t = input("hit or stand. ")
        while(t == "hit"):
            
            self.cards.append(self.shuffler.deal())
            print(str(self))
            t = input("hit or stand. ")

    def won(self):
        mx = 0
        t = 0
        index = 0
        
        for i in range(len(self.players)):
            t = 0
            for j in range(len(self.players[i].cards)):
                if(self.players[i].cards[j].faceIndex > 10):
                    t = self.players[i].cards[j].faceIndex - 10
                if(self.players[i].cards[j].faceIndex == 0):
                    st = input("use as 11 or 1")
                        
                t += self.players[i].cards[j].faceIndex + 1
                
                if(t < 22):
                    if(t > mx):
                        mx = t
                        index = i + 1
                        
        t = 0
        for i in range(len(self.cards)):
            t += self.cards[i].faceIndex + 1
             
        if(t < 22):
            if(t > mx):
                mx = t
                index = -1
                    
        if(index == -1):
            print("Dealer wins")
        else:
            print("player " + str(index) + " wins")
         
                
