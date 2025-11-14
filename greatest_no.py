var_a=int(input("enter 1st no. :"))
var_b=int(input("enter 2nd no. :"))
var_c=int(input("enter 3rd no. :"))
if (var_a >= var_b) and (var_a >= var_c):
	var_great = var_a
elif (var_b>=var_a) and (var_b >= var_c):
	var_great = var_b
else:
	var_great =var_c
print(var_great,"is greatest among", var_a,",",var_c)