start_value=int(input("enter starting range:"))
end_value=int(input("enter ending range:"))
for i in range(start_value,end_value+1):
	for j in range(2,i):
		if i%j==0:
			print("{} is composite".format(i))
			break
		else :
			print("{} is prime".format(i))
  