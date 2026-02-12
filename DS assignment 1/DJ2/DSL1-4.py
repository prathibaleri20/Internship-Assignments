#A program to accept 3 subject marks and calculate total, average and print it with appropriate message

phy=int(input("enter physics marks"))
mat=int(input("enter maths marks"))
che=int(input("enter chemistry marks"))
tot=phy+mat+che
avg=tot/3
print("physics marks=",phy)
print("maths marks=",mat)
print("chemistry marks=",che)
print("total=",tot)
print("average=",avg)
