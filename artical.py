#articals counter
x=input("enter sentence :")
y=x.split(" ")
a_counter=0
an_counter=0
the_counter=0
for i in y:
	if i=="a":
		a_counter=a_counter+1
	elif i=="an":
		an_counter=an_counter+1
	elif i=="the":
		the_counter=the_counter+1
print("A Count :",a_counter)
print("An Count :",an_counter)
print("The Count :",the_counter)	