try:
	a=int(input("enter value:"))
	b=int(input("enter value:"))
	c=int(input("enter value:"))
	if a>b and a>c:
		print("a is greatest")
	elif b>a and b>c:
		print("b is greatest")
	else:
		print("c is greatest")
except ValueError :
	print("Only Integer value are allowed")
finally:
	print("exection completed succesfully")