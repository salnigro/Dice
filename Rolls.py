import random
roll = [0,0,0,0,0,0]
n = int(input("Enter number of Dice: "))
x = 0
def Dicerolls(n):
	for i in range(0,n):
		x = random.randrange(1,6,1)
		print(str(x))
		roll[x-1] = roll[x-1]+1

Dicerolls(n)
print("1: " + str(roll[0]) + "/" + str(n))
print("2: " + str(roll[1]) + "/" + str(n))
print("3: " + str(roll[2]) + "/" + str(n))
print("4: " + str(roll[3]) + "/" + str(n))
print("5: " + str(roll[4]) + "/" + str(n))
print("6: " + str(roll[5]) + "/" + str(n))
