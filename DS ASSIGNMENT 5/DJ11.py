class calculate:
    a = int(input("enter the first number"))
    b = int(input("enter second number"))
    c = 0

    def add(me):
        print(me.a)
        print(me.b)
        me.c = me.a + me.b
        print(me.c)
obj = calculate()
obj.add()



class calculate:
    a = int(input("enter the first number"))
    b = int(input("enter second number"))
    c = 0

    def add(me):
        print(me.a)
        print(me.b)
        me.c = me.a + me.b
        print(me.c)

    def subt(me):
        print(me.a)
        print(me.b)
        me.c = me.a - me.b
        print(me.c)
obj = calculate()
obj.add()
obj.subt()




class calculate:
    a = int(input("enter the first number"))
    b = int(input("enter second number"))
    c = 0

    def add(me):
        print(me.a)
        print(me.b)
        me.c = me.a + me.b
        print(me.c)

    def subt(me):
        print(me.a)
        print(me.b)
        me.c = me.a - me.b
        print(me.c)

    def mult(me):
        print(me.a)
        print(me.b)
        me.c = me.a * me.b
        print(me.c)

    def divide(me):
        print(me.a)
        print(me.b)
        me.c = me.a / me.b
        print(me.c)
obj = calculate()
obj.add()
obj.subt()
obj.mult()
obj.divide()

class calculate:
    a = int(input("enter the first number"))
    b = int(input("enter second number"))
    c = 0

    def add(me):
        print(me.a)
        print(me.b)
        me.c = me.a + me.b
        print(me.c)

    def subt(me):
        print(me.a)
        print(me.b)
        me.c = me.a - me.b
        print(me.c)

    def mult(me):
        print(me.a)
        print(me.b)
        me.c = me.a * me.b
        print(me.c)

    def divide(me):
        print(me.a)
        print(me.b)
        me.c = me.a / me.b
        print(me.c)

obj = calculate()
print("1. to perform addition press 1")
print("2. to perform subtraction press 2")
print("3. to perform multiplication press 3")
print("4. to perform division press 4")
opt = int(input("enter your choice"))
if (opt == 1):
    obj.add()
elif (opt == 2):
    obj.subt()
elif (opt == 3):
    obj.mult()
elif (opt == 4):
    obj.divide()
else:
    print("invalid option")



class contacts:
    name = input("enter your name")
    ph = int(input("enter the phone number"))

    def save(me):
        print(me.name)
        print(me.ph)


class whatsapp:
    name = input("enter your name")
    ph = int(input("enter the phone number"))
    msg = input("type the message")

    def send(me):
        print(me.name)
        print(me.ph)
        print(me.msg)
obj1 = contacts()
obj1.save()
obj2 = whatsapp()
obj2.send()
















