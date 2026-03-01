n=eval(input("enter value:"))
if type(n) in [int,float,complex,bool]:
	print("data is single value")
else:
	print("data is multi-value")
