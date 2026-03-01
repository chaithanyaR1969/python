x=int(input("enter a value1:"))
y=int(input("enter a value2:"))
if x>=0 and y>=0:
	print("it is present in 1st quadrent")
elif x>=0 and y<0:
	print("it is present in 2nd quadrent")
elif x<0 and y<0:
	print("it is present in 3rd quadrent")
else:
	print("it is present in 4th quadrent")