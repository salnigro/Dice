from Card import Card

class Player(object):

    

    def __init__(self,chips):
        self.cards = []
        self.bet = 0
        self.chips = chips
        
        
    def betCh(self,n):
        self.bet = n
        self.chips = self.chips - self.bet
        
    def won(self,n):
        self.bet = 0
        self.chips += n
        
    def __str__(self):
        return ', '.join(str(card) for card in self.cards)
    
        
