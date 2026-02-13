def student(name):
	print(name)
student("vikas")

def student(name,age):
	print(name)
	print(age)

student("vikas",23)

def student(name,age,mrks):
	print(name)
	print(age)
	print(mrks)
student("vikas",23,67.45)


def f(num):
    return num ** 2 + 1
print(f(4))


def f(num):
    return num ** 2 + 1
x = f(4)
print(x)


def f(num):
    return num ** 2 + 1
x = f(4)
z = x + 100
print(z)


def f(num):
    return num ** 2 + 1
x = f(4)
z = x + 100
print(z)

def f(num):
        return num**2 + 1
x=f(4)
w=int(input("enter any number="))
z=x+w
print(z)

def add(x,y):
	return x+y
x=add(768,654)
print(x)

def add(x,y):
	return x+y


a=int(input("enter the first number="))
b=int(input("enter the second number="))
x=add(a,b)
print(x)

def add(x,y,z):
	return x+y*z


a=int(input("enter the first number="))
b=int(input("enter the second number="))
c=int(input("enter the third number="))
x=add(a,b,c)
print(x)


def add(x, pi=3.142):
	return x * pi


a = int(input("enter the first number="))
x = add(a)
print(x)



def student(name, course, collname="cmr"):
	return name, course, collname
s1 = student("vikas", "mba")
print(s1)



def student(name, course, collname="cmr"):
	return name, course, collname
s1 = student("vikas", "mba")
s2 = student("sanjay", "btech")
print(s1)
print(s2)



def student(name, course, collname="cmr"):
	return name, course, collname
s1 = student("vikas", "mba")
s2 = student("sanjay", "btech")
print(s1)
print(s2)
x1 = student("pooja", "bcom", "kle")
x2 = student("kavya", "bba", "kle")
print(x1)
print(x2)

