#Inheritance 
class addition:	         #Base Class / Parent Class
	a=int(input("enter the first number"))
	b=int(input("enter second number"))
	c=0
	
	def add(me):
		print(me.a)
		print(me.b)
		me.c=me.a+me.b
		print(me.c)

class subtract(addition):   
	#Derived class
	x=int(input("enter the first number"))
	y=int(input("enter second number"))
	z=0
	
	def subt(me):
		print(me.x)
		print(me.y)
		me.z=me.x-me.y
		print(me.z)	

obj=subtract()
obj.add()
obj.subt()

print("______")
class cmr:
	cname="cmr college"

	def f1(me):
		print(me.cname)

class course(cmr):
	c1="bba"
	c2="mba"
	c3="be"
	c4="mtech"
	
	def f2(me):
		print(me.c1)
		print(me.c2)
		print(me.c3)
		print(me.c4)
obj=course()
obj.f1()
obj.f2()
print("______-------------------------")


class father:
	
	def f1(me):
		print("this is parent class")


class son(father):

	def s1(me):
		print("this is derived class")


obj1=son()

obj1.f1()
obj1.s1()
print("-------------------------------------------------------------------------")
class father:
	
	def f1(me):
		print("this is parent class")
		print("works in wipro")
		print("father's age=50")
		print("stays in jayanagar")


class son(father):

	def s1(me):
		print("this is derived class")
		print("studies in cmr college")
		print("son's age=23")


obj1=son()
obj1.f1()
obj1.s1()










