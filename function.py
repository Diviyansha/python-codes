#!/root/Desktop/python
def factorial(num):
	if(num==1):
		return num
	else:
		num*factorial(num-1)
num= int(raw_input("enter number"))
if num<0:
	print "the factorial cannot be calculated"
elif num=0:
	print " the factorial is 0"
else:
	print "the factorial is",factorial(num)

