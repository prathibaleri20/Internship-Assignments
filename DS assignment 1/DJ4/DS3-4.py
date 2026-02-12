#PROGRAM TO FIND THE LARGEST AND SMALLEST OF 3 NUMBERS
print("Finding Largest number")
a=int(input("enter first number"))
b=int(input("enter second number"))
c=int(input("enter third number"))

if (a>b) & (a>c):
	print("the first number is highest")
elif (b>a) & (b>c):
	print("the second number is highest")
else:
	print("the third number is highest")


#Smallest number
print("Finding smallest number")
if (a<b) & (a<c):
	print("the first number is lowest")
elif((b<a) & (b<c)):
    print("the second number is lowest")
else:
    print("the third number is lowest")