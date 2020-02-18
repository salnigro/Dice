from random import randint, random
from math import floor

deck = []
suits = ["♦","♣","♥","♠"]
for i in range(4):
    for j in range(1,14):
        value = str(j)
        if( j == 1):
            value =  "A"
        if(  j == 11):
            value =  "J"
        if(  j == 12):
            value =  "Q"
        if( j == 13):
            value =  "K"
        deck.append(f"{value}{suits[i]}")
            


def shuffle(arr):
    n = len(arr)
    while n > 1:
        i = int(floor(random() * n))
        n -= 1
        arr[i], arr[n] = arr[n], arr[i]
    return the_list


shuffle(deck)

print(deck)
