class addition:
    a = int(input("enter the first number"))
    b = int(input("enter second number"))
    c = 0

    def add(me):
        print(me.a)
        print(me.b)
        me.c = me.a + me.b
        print(me.c)


class subtraction:
    a = int(input("enter the first number"))
    b = int(input("enter second number"))
    c = 0

    def subt(me):
        print(me.a)
        print(me.b)
        me.c = me.a - me.b
        print(me.c)
obj1 = addition()
obj1.add()
obj2 = subtraction()
obj2.subt()


class addition:
    a = int(input("enter the first number"))
    b = int(input("enter second number"))
    c = 0

    def add(me):
        print(me.a)
        print(me.b)
        me.c = me.a + me.b
        print(me.c)


class subtraction:
    a = int(input("enter the first number"))
    b = int(input("enter second number"))
    c = 0

    def subt(me):
        print(me.a)
        print(me.b)
        me.c = me.a - me.b
        print(me.c)


class multiply:
    a = int(input("enter the first number"))
    b = int(input("enter second number"))
    c = 0

    def mult(me):
        print(me.a)
        print(me.b)
        me.c = me.a * me.b
        print(me.c)


class divide:
    a = int(input("enter the first number"))
    b = int(input("enter second number"))
    c = 0

    def divi(me):
        print(me.a)
        print(me.b)
        me.c = me.a / me.b
        print(me.c)


obj1 = addition()
obj1.add()
obj2 = subtraction()
obj2.subt()
obj3 = multiply()
obj3.mult()
obj4 = divide()
obj4.divi()




class addition:
    a = int(input("enter the first number"))
    b = int(input("enter second number"))
    c = 0

    def add(me):
        print(me.a)
        print(me.b)
        me.c = me.a + me.b
        print(me.c)


class subtraction:
    a = int(input("enter the first number"))
    b = int(input("enter second number"))
    c = 0

    def subt(me):
        print(me.a)
        print(me.b)
        me.c = me.a - me.b
        print(me.c)


class multiply:
    a = int(input("enter the first number"))
    b = int(input("enter second number"))
    c = 0

    def mult(me):
        print(me.a)
        print(me.b)
        me.c = me.a * me.b
        print(me.c)


class divide:
    a = int(input("enter the first number"))
    b = int(input("enter second number"))
    c = 0

    def divi(me):
        print(me.a)
        print(me.b)
        me.c = me.a / me.b
        print(me.c)


print("1. to perform addition press 1")
print("2. to perform subtraction press 2")
print("3. to perform multiplication press 3")
print("4. to perform division press 4")
opt = int(input("enter your choice"))
if (opt == 1):
    obj1 = addition()
    obj1.add()
elif (opt == 2):
    obj2 = subtraction()
    obj2.subt()
elif (opt == 3):
    obj3 = multiply()
    obj3.mult()
elif (opt == 4):
    obj4 = divide()
    obj4.divi()
else:
    print("invalid option")

