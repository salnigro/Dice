from random import randint, random
from math import floor
import sys 
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
    return arr


def deal():
    d = []
    s = ["♦","♣","♥","♠"]
    f = {1:"A", 11:"J",12:"Q",13:"K"}
    for i in range(4):
        for j in range(1,14):
            d.append(f"{f[j] if j in f else j}{s[i]}")
    return d



def selectSort(arr):
    
    for i in range(len(arr)):
        
        min_idx = i
        
        for j in range(i+1, len(arr)):
            s = arr[min_idx][0:len(arr[min_idx])-1]

            t = arr[j]
            t = t[0:len(t)-1]
            if(t == "A"):
                t="1"
            if(t == "J"):
                t="11"
            if(t == "Q"):
                t="12"
            if(t == "K"):
                t="13"
            if(s == "A"):
                s="1"
            if(s == "J"):
                s="11"
            if(s == "Q"):
                s="12"
            if(s == "K"):
                s="13"
            if int(s) > int(t):
                
                min_idx = j 
                
        arr[i], arr[min_idx] = arr[min_idx], arr[i] 








def proper(s):
    if(len(s) == 2):
        s = s[0:1]
        if(s == "A"):
            s="1"
        if(s == "J"):
            s="11"
        if(s == "Q"):
            s="12"
        if(s == "K"):
            s="13"
    if(len(s) == 3):
        s = s[0:2]
    return int(s)

shuffle(deck)

selectSort(deck)

print(deck)








