deck = []
suits = ["♦","♣","♥","♠"]
for i in range(4):
    for j in range(1,14):
        value = str(j)
        if( i == 1):
            value =  "A"
        if( i == 11):
            value =  "J"
        if( i == 12):
            value =  "Q"
        if( i == 13):
            value =  "K"
        deck.append(f"{value}{suits[i]}")
            
        
print(deck)
