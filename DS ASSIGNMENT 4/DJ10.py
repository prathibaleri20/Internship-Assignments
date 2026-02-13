def add():
	a=89
	b=77
	c=a+b
	print(a)
	print(b)
	print(c)
add()

def x1():
	a=89
	b=77
	c=a+b
	print(a)
	print(b)
	print(c)
x1()

#PROGRAM TO ADD AND SUBTRACT
def add():
	a=89
	b=77
	c=a+b
	print(a)
	print(b)
	print(c)

def subtract():
	a=89
	b=77
	c=a-b
	print(a)
	print(b)
	print(c)
add()
subtract()

#USER INPUT
def add():
	a=int(input("enter first number"))
	b=int(input("enter second number"))
	c=a+b
	print(a)
	print(b)
	print(c)
add()

def add():
	a=float(input("enter first number"))
	b=float(input("enter second number"))
	c=a+b
	print(a)
	print(b)
	print(c)
add()

def name():
	fn=input("enter first number")
	ln=input("enter second number")
	c=fn+" "+ln
	print(fn)
	print(ln)
	print(c)
name()

#DIVISION ADDITION SUBTRACTION
def add():
	a=int(input("enter first number"))
	b=int(input("enter second number"))
	c=a+b
	print(a)
	print(b)
	print(c)

def subtract():
	a=int(input("enter first number"))
	b=int(input("enter second number"))
	c=a-b
	print(a)
	print(b)
	print(c)

def multiply():
	a=int(input("enter first number"))
	b=int(input("enter second number"))
	c=a*b
	print(a)
	print(b)
	print(c)

def divide():
	a=int(input("enter first number"))
	b=int(input("enter second number"))
	c=a/b
	print(a)
	print(b)
	print(c)
add()
subtract()
multiply()
divide()

#SWITCH CASE DEMO
def add():
	a=int(input("enter first number"))
	b=int(input("enter second number"))
	c=a+b
	print(a)
	print(b)
	print(c)

def subtract():
	a=int(input("enter first number"))
	b=int(input("enter second number"))
	c=a-b
	print(a)
	print(b)
	print(c)

def multiply():
	a=int(input("enter first number"))
	b=int(input("enter second number"))
	c=a*b
	print(a)
	print(b)
	print(c)

def divide():
	a=int(input("enter first number"))
	b=int(input("enter second number"))
	c=a/b
	print(a)
	print(b)
	print(c)
print("1. Addition")
print("2. Subtraction")
print("3. multiply")
print("4. Division")
opt=int(input("enter your choice"))
if (opt==1):
	add()
elif (opt==2):
	subtract()
elif (opt==3):
	multiply()
elif (opt==4):
	divide()
else:
	print("Invalid choice")

#find highest no
def f1():
    x = int(input("enter first number"))
    y = int(input("enter second number"))
    if (x > y):
        print("the first number is highest")
    else:
        print("the second number is highest")

f1()

#for loop
def f1():
    for i in range(1, 11):
        print(i)
f1()


def f1():
    s1 = [23, 45, 55, 66, 77]
    for i in s1:
        print(i)
f1()

def student():
	rno=int(input("enter any roll number"))
	name=input("enter student name")
	phy=int(input("enter physics marks"))
	mat=int(input("enter maths marks"))
	che=int(input("enter chemistry marks"))
	total=phy+mat+che
	avg=total/3
	print(rno)
	print(name)
	print(phy)
	print(mat)
	print(che)
	print(total)
	print(avg)
student()