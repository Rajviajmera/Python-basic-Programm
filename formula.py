print("welcome formula program")
print("following formula available")
choice=int(input("press 1 for (a+b)^2=(a*a)+(b+b)+(2*a*b),2 for (a-b)^2=(a*a)+(b*b)-(2*a*b),3 for (a*a)-(b*b)=(a+b)(a-b),4 for (x+a)(x+b),Enter value: "))
if choice==1:
	a=int(input("enter any value:"))
	b=int(input("enter any value:"))
	result=(a*a)+(b*b)+(a*b)
	print(result)
elif choice==2:
	a=int(input("enter any value:"))
	b=int(input("enter any value:"))
	result=(a*a)+(b*b)-(2*a*b)
	print(result)
elif choice==3:
	a=int(input("enter any value:"))
	b=int(input("enter any value:"))
	result=(a+b)(a-b)
	print(result)
elif choice==4:
	x=int(input("enter any value:"))
	a=int(input("enter any value:"))
	b=int(input("enter any value:"))
	result=(x+a)(x+b)
else:
	print("invalid number")