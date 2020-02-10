import random

n = int(input("Enter number of Dice: "))

def Dicerolls(n):
	for i in range(0,n):
		print(random.randrange(1,6,1))

Dicerolls(n)
