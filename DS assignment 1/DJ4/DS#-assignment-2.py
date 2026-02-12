
#FIND SMALLEST OF 4 NUMBERS
print("Program to smallest of 4 numbers")
n1=int(input("Enter 1st no"))
n2=int(input("Enter 2nd no"))
n3=int(input("Enter 3rd no"))
n4=int(input("Enter 4th no"))
if(n1<n2 and n1<n3 and n1<n4):
    print("1st no is lowest")
elif (n2<n3 and n2<n4):
    print("2nd no is lowest")
elif(n3<n4):
    print("3rd no is lowest")
else:
    print("4th no is lowest")

