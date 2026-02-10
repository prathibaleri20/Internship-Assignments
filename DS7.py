#DEMONSTRATION OF TUPLES
t1=(11,22,33,44,55,66,77,88)
print(t1)

s1=(11,22,33,'aa','bb','cc',33,66)
print(s1)

s1=(11,22,33,'aa','bb','cc',33,66)
for i in s1:
    print(i)

#printing data according to index value
s1=(11,22,33,'aa','bb','cc',33,66)
print(s1[2])

#slicing in Tuple---All slicing concepts can be implemeted on Tuple
#to print 1 to 5 values

s1=(11,22,33,'aa','bb','cc',33,66)
print(s1[1:5])

#pop(), remove()---Can not be used in Tuple SO WE USE DEL
s1=(11,22,33,'aa','bb','cc',33,66)
del s1

#converting Tuple to List data
s1=(11,22,33,'aa','bb','cc',33,66)
print(s1)
x1=list(s1)
print(x1)

#converting List data to Tuple
x1=[11,22,33,'aa','bb','cc',33,66]
print(x1)
s1=tuple(x1)
print(s1)

#to find the length(Number of values) of the data in Tuple
s1=(11,22,33,'aa','bb','cc',33,66)
print(len(s1))

#slicing a part of data from Tuple and storing it into another Tuple
s1=(11,22,33,'aa','bb','cc',33,66)
print(s1)

s2=s1[2:4]
print(s2)

#Elements sliced from 3rd element till the end:
s1=(11,22,33,'aa','bb','cc',33,66)
print(s1)

s2=s1[3:]
print(s2)

#to store & print whole TUPLE with the use of slicing operation, use [:]
s1=(11,22,33,55,88,33,66)
print(s1)

s2=s1[:]
print(s2)

s1=(11,22,33,55,88,33,66)
print(s1)

#SLICING IN REVERSE ORDER
s2=s1[::-1]
print(s2)

#counting number of occurances of data
s1=(11,22,33,55,88,33,66)
print(s1)
print(s1.count(33))

#searching  for a particular data in tuple
s1=(11,22,33,55,88,33,66)
print(s1)
x=int(input("enter data to be searched"))
for i in s1:
    if (x==i):
        print("data found")
        break
else:
    print("data not found")

# searching for particular data in list and print the index value of the data(use index() built in function)--in TUPLE
s1=(11,22,33,55,88,33,66)
print(s1)

x=int(input("enter data to be searched"))
for i in s1:
    if (x==i):
        print("data found",s1.index(i))
        break
else:
    print("data not found")









































































