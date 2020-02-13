import random
import array
b = [0,0]
x = [0]
t = int(input("How many flips to simulate? "))
l = 0
for i in range(1,t):
	x.append(0)

for i in range(0,t):
	x[i] = random.randrange(0,2)
for i in range(0,len(x)-2):
	if(x[i]==0):
		if(x[i+1]==0):
			b[0] = b[0] + 1
	if(x[i]==1):
		if(x[i+1]==1):
			b[1] = b[1] + 1

print("number of h in row " + str(b[0]))

print("number of t in row " + str(b[1]))

#for i in range(0,t-1):
#	print("t" + str(x[i]))
#print("1: " + str(x[0]) + "/" + str(t) + " = " + str((x[0]/t)*100) + "%")
#print("2: " + str(x[1]) + "/" + str(t) + " = " + str((x[1]/t)*100) + "%")
