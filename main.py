from random import randint, random
from math import floor
from Card import Card
from Deck import Deck
from Shuffler import Shuffler
from Dealer import Dealer
from Player import Player
import sys




decks = [Deck(),Deck(),Deck()]
players = [Player(100)]
Cdeck = Shuffler(decks)

dave = Dealer(players,Cdeck)

dave.deal()


#print(Cdeck)




