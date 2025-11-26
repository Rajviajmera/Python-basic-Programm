# write a py script of to find all multipal of x from a user defind range
x=int(input("enter x value:"))
start_value=int(input("enter starting range:"))
end_value=int(input("enter ending range:"))
for i in range(start_value,end_value+1):
	if i%x==0:
		print(i)