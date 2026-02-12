#program to find highest and 2nd highest of 3 numbers
n1=int(input("Enter 1st no"))
n2=int(input("Enter 2nd no"))
n3=int(input("Enter 3rd no"))
if n1>n2 and n1>n3:
    print("1st no is highest")
    if n2>n3:
        print("2nd no is 2nd highest")
    else:
        print("3rd no is 2nd highest")
elif n2>n3:
    print("2nd no is highest")
    if n1>n3:
        print("3rd no is second highest")
    else:
        print("4th no is second highest")
else:
    print("3rd no is highest")
    if n1>n2:
        print("1st no is second highest")
    else:
        print("2nd no is second highest")


