class gf:
	def f1(me):
		print("this is grand father class")

class father(gf):
	def f2(me):
		print("this is father class")

class son(father):
	def f3(me):
		print("this is son class")

obj=son()
obj.f1()
obj.f2()
obj.f3()
print("------------------")

class first:
	def f1(me):
		print("this is first class")

class second(first):
	def f2(me):
		print("this is second class")

class third(second):
	def f3(me):
		print("this is third class")

obj=third()
obj.f3()
obj.f2()
obj.f1()
print("--------")

class first:
	def f1(me):
		print("this is first class")

class second(first):
	def f2(me):
		print("this is second class")

class third(second):
	def f3(me):
		print("this is third class")

obj=third()
obj.f3()
obj.f1()
print("--------")

class addition:
	a=99
	b=77
	c=a+b
	def add(me):
		print(me.a)
		print(me.b)
		print(me.c)

class subtract(addition):
	x=66
	y=44
	z=x-y
	def subt(me):
		print(me.x)
		print(me.y)
		print(me.z)

class multiply(subtract):
	p=99
	q=55
	r=p*q
	def mult(me):
		print(me.p)
		print(me.q)
		print(me.r)
obj=multiply()
obj.add()
obj.subt()
obj.mult()

print("----------------")

class addition:
	a=int(input("enter first number"))
	b=int(input("enter second number"))
	c=a+b
	def add(me):
		print(me.a)
		print(me.b)
		print(me.c)

class subtract(addition):
	x=int(input("enter first number"))
	y=int(input("enter second number"))
	z=x-y
	def subt(me):
		print(me.x)
		print(me.y)
		print(me.z)

class multiply(subtract):
	p=int(input("enter first number"))
	q=int(input("enter second number"))
	r=p*q
	def mult(me):
		print(me.p)
		print(me.q)
		print(me.r)
obj=multiply()
obj.add()
obj.subt()
obj.mult()
print("--------------------------------------------------------")

class addition:
	a=0
	b=0
	c=0
	def add(me):
		me.a=int(input("enter first number"))
		me.b=int(input("enter second number"))
		me.c=me.a+me.b
		print(me.a)
		print(me.b)
		print(me.c)

class subtract(addition):
	x=0
	y=0
	z=0
	def subt(me):
		me.x=int(input("enter first number"))
		me.y=int(input("enter second number"))
		me.z=me.x-me.y
		print(me.x)
		print(me.y)
		print(me.z)

class multiply(subtract):
	p=0
	q=0
	r=0
	def mult(me):
		me.p=int(input("enter first number"))
		me.q=int(input("enter second number"))
		me.r=me.p*me.q
		print(me.p)
		print(me.q)
		print(me.r)
obj=multiply()
obj.add()
obj.subt()
obj.mult()

print("------------------")
#multi - level inheritance	----> USING CONSTRUCTOR 

class addition:
    a=0
    b=0
    z=0
    def __init__(me):        
        me.a=int(input("enter first number for addition"))
        me.b=int(input("enter second number for addition"))    
        me.z=me.a+me.b    
        print(me.z)

class subtraction(addition):
    x=0
    y=0
    z1=0
    def __init__(me):
        super().__init__()        #calls the immediate constructor of base class
        me.x=int(input("enter first number for subtraction"))
        me.y=int(input("enter second number for subtraction"))    
        me.z1=me.x-me.y    
        print(me.z1)
        
class multiply(subtraction):
    x1=0
    y1=0
    z2=0
    def __init__(me):
         super().__init__()       
		#calls the immediate constructor of base class
         me.x1=int(input("enter first number for multiply"))
         me.y1=int(input("enter second number for multiply"))    
         me.z2=me.x1*me.y1    
         print(me.z2)
     
obj1=multiply()


