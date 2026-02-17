
class calculate:
    a = int(input("enter the first number"))
    b = int(input("enter second number"))
    c = 0

    def __init__(me):
        print(me.a)
        print(me.b)
        me.c = me.a + me.b
        print(me.c)


obj = calculate()


class highest:
    a = int(input("enter the first number"))
    b = int(input("enter second number"))

    def __init__(me):
        if (me.a > me.b):
            print("first number is highest")
        else:
            print("second number is highest")


obj = highest()


# constructor in python ---USE __init__

class addition:
    a = int(input("enter first number"))
    b = int(input("enter second number"))
    z = a + b

    def __init__(me):
        print(me.a)
        print(me.b)
        print(me.z)


obj1 = addition()
print("-----------------------------------------------------------------------------------")

class addition:
    a = int(input("enter first number"))
    b = int(input("enter second number"))
    z = a + b

    def __init__(me):
        print(me.a)
        print(me.b)
        print(me.z)

    def __del__(me):
        print("memory cleared")


obj1 = addition()


class student:
    def __init__(me, name):
     print(name)
obj1 = student('sanjay')

class student:
    def __init__(me, name, age):
        print(name)
        print(age)
obj1 = student('sanjay', 19)


class student:

    def __init__(me, name, age, course):
        print(name)
        print(age)
        print(course)


obj1 = student('sanjay', 19, 'MBA')


class student:

    def __init__(me, name, age, course):
        print("student name= ", name)
        print("student age= ", age)
        print("student course= ", course)


obj1 = student('sanjay', 19, 'MBA')


#passing 4 parameters

class student:

    def __init__(me, name, age, course, cname):
        print("student name= ", name)
        print("student age= ", age)
        print("student course= ", course)
        print("college name= ", cname)


obj1 = student('sanjay', 19, 'MBA', 'CMR')


#parameters and create object
class student:

    def __init__(me, name):
        print(name)


obj1 = student('sanjay')
obj2 = student('pooja')



class cmr:

    def __init__(me, name, age, course):
        print("student name= ", name)
        print("student age= ", age)
        print("student course= ", course)


obj1 = cmr('sanjay', 19, 'MBA')
obj2 = cmr('pooja', 22, 'MCA')
obj3 = cmr('Harshitha', 20, 'BCOM')


class cmr:

    def __init__(me, name, age, course):
        print("student name= ", name)
        print("student age= ", age)
        print("student course= ", course)


class pes:

    def __init__(me, name, age, course):
        print("student name= ", name)
        print("student age= ", age)
        print("student course= ", course)


print("CMR college Students List")
obj1c = cmr('sanjay', 19, 'MBA')
obj2c = cmr('pooja', 22, 'MCA')
obj3c = cmr('Harshitha', 20, 'BCOM')

print("PES college Students List")
obj1p = pes('Raghu', 21, 'BE')
obj2p = pes('Sham', 22, 'MTech')
obj3p = pes('Satish', 20, 'BBM')

