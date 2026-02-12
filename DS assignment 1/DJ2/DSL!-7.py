#A program to accept and print complete marks sheet

rno=int(input("enter roll number"))
name=input("enter student name")
phy=int(input("enter physics marks"))
mat=int(input("enter maths marks"))
che=int(input("enter chemistry marks"))
tot=phy+mat+che
avg=tot/3
print("roll no=",rno);
print("student name=",name)
print("physics marks=",phy)
print("maths marks=",mat)
print("chemistry marks=",che)
print("total=",tot)
print("average=",avg)
