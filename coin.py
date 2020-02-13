import random
x = [0,0]
t = int(input("How many flips to simulate? "))
l = 0
for i in range(0,t):
	l = random.randrange(1,3) 
	x[l-1] = x[l-1] + 1


print("1: " + str(x[0]) + "/" + str(t) + " = " + str((x[0]/t)*100) + "%")
print("2: " + str(x[1]) + "/" + str(t) + " = " + str((x[1]/t)*100) + "%")
