import random
import array
b = []
x = [0]
k = 0;
t = int(input("How many flips to simulate? "))
g = int(input("Which side are you looking for (0-heads,1-tails)? "))
h = int(input("How long is the sequence you're looking for? "))
#l = 0
for i in range(0,h):
	b.append(g)
#print(str(b[0:h]))
for i in range(1,t):
	x.append(0)

for i in range(0,t):
	x[i] = random.randrange(0,2)
#	print(str(x[i]) + " x")
for i in range(0,len(x)):
#	print(str(x[i:i+h]) + " x[]")
#	print(str(b[0:h+1]) + " b")
	if x[i:i+h] == b[0:h+1]:
		k = k + 1
#		print(str(x[i:i+h]) + " x[] " + str(i))
print(str(b[0:h+1]) + " occurs " + str(k) + " times")


#	if(x[i]==g):
#		if(x[i+1]==g):
#			b[0] = b[0] + 1
#	if(x[i]==1):
#		if(x[i+1]==1):
#			b[1] = b[1] +1

#print("number of h in row " + str(b[0]))

#print("number of t in row " + str(b[1]))

#for i in range(0,t-1):
#	print("t" + str(x[i]))
#print("1: " + str(x[0]) + "/" + str(t) + " = " + str((x[0]/t)*100) + "%")
#print("2: " + str(x[1]) + "/" + str(t) + " = " + str((x[1]/t)*100) + "%")
