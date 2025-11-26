#mean
def mean():
	n=int(input("enter value of total no:"))
	sum=0
	for i in range (n):
		term=int(input("enter value:"))
		sum=sum+term
	mean=sum/n
	print("mean",mean)
#for l in range(10):
mean()
#median
def median():
	n=int(input("enter median value:"))
	median=((n+1)/2)
	print("median",median)
#for  j in range(10):
median()


#mode
def mode():
	L=int(input("enter mode value:"))
	f0=int(input("enter fec0:"))
	f1=int(input("enter fec1:"))
	f2=int(input("enter fec2:"))
	h=int(input("enter value h:"))
	Mode = L +( ((f1 - f0) / ((2*f1) - f0 - f2)) * h)
	print(mode)
#for k in range(10):
mode()