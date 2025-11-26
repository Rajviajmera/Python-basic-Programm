choice= input("enter 1 for convert 1 bit into byte\nenter 2 for convert 1 byte into bit\nenter valid choice: ")
if choice=="1":
	bit=int(input("enter number of bit:"))
	x=bit*0.125
	print("{} bit ={} byte".format(bit,x))
elif choice=="2":
	byte=int(input("enter number of byte:"))
	y=byte*8
	print("{} byte = {} bit".format(byte,y))
else :
	print("enter valid choice")