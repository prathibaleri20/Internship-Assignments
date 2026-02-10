#Find the highest and smallest  of 4 nos
n1=int(input("Enter 1st no"))
n2=int(input("Enter 2nd no"))
n3=int(input("Enter 3rd no"))
n4=int(input("Enter 4th no"))
print("Finding large value")
if(n1>n2 and n1>n3 and n1>n4):
    print("1st no is highest")
elif (n2>n3 and n2>n4):
    print("2nd no is highest")
elif(n3>n4):
    print("3rd no is highest")
else:
    print("4th no is highest")
print("finding small value")
if(n1<n2 and n1<n3 and n1<n4):
    print("1st no is smallest")
elif (n2<n3 and n2<n4):
    print("2nd no is smallest")
elif(n3<n4):
    print("3rd no is smallest")
else:
    print("4th no is smallest")


