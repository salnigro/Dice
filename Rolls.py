import random
roll = [0,0,0,0,0,0]
n = int(input("Enter number of Dice: "))
x = 0
def Dicerolls(n):
	for i in range(0,n):
		x = random.randrange(1,7,1)
		roll[x-1] = roll[x-1]+1

Dicerolls(n)
print("1: " + str(roll[0]) + "/" + str(n) + " = " + str((roll[0]/n)*100) + "%")
print("2: " + str(roll[1]) + "/" + str(n) + " = " + str((roll[1]/n)*100) + "%")
print("3: " + str(roll[2]) + "/" + str(n) + " = " + str((roll[2]/n)*100) + "%")
print("4: " + str(roll[3]) + "/" + str(n) + " = " + str((roll[3]/n)*100) + "%")
print("5: " + str(roll[4]) + "/" + str(n) + " = " + str((roll[4]/n)*100) + "%")
print("6: " + str(roll[5]) + "/" + str(n) + " = " + str((roll[5]/n)*100) + "%")
