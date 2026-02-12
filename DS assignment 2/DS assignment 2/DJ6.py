#Lists
x1=[11,22,33,44,55]
a1=["raghu","sham","ravi","pooja"]
print(x1)
print(a1)

#using for accessing
x1=[11,22,33,44,55,66]
for i in x1:
	print(i)

s1=["aa","bb",11,22,33,78.23,89.11]
for i in s1:
	print(i)

s1=["aa","bb",11,22,33,78.23,89.11]
print(s1[2])
print(s1[1])
print(s1[0])
print(s1[3])
print(s1[4])

#Use of append()
s1=['aa','bb','cc',123,456,78.93,56.77]
s2=[]
for i in s1:
    s2.append(i)
print (s2)

s1=['aa','bb','cc',123,456,78.93,56.77]
print(s1)
s2=[100,200,300]
s2.append(s1)
print(s2)

s1=['aa','bb','cc',123,456,78.93,56.77]
print(s1)
s2=[100,200,300]
s2.extend(s1)     #THIS HELPS TO ADD AT LAST
print(s2)

#USE OF REMOVE
s1=['aa','bb','cc',123,456,78.93,56.77]
print(s1)
s1.remove("cc")
print(s1)
s1.remove(123)
print(s1)

#USE OF POP  (CAN BE USED FOR STACK OPERATIONS)
s1=['aa','bb','cc',123,456,78.93,56.77]
print(s1)
print(len(s1))
s1.pop(2)
print(s1)
print(len(s1))

#DEMONSTRATION OF SLICING
s1=['aa','bb','cc',123,456,78.93,56.77]
print(s1)
s2=[]
s2=s1[3:5]
print(s2)

s3=[]
s3=s1[3:]  #access last 3 elements
print(s3)

s4=[]
s4=s1[:]        #to copy entire list
print(s4)

s1=['aa','bb','cc',123,456,78.93,56.77]
print(s1)

#copy in reverse order
s2=[]
s2=s1[::-1]
print(s2)

#use of len()
s1=['aa','bb','cc',123,456,78.93,56.77]
print(s1)
print(len(s1))

#use of count()
s1=['aa','bb','cc','cc',123,456,'cc',78.93,56.77]
print(s1)
print(s1.count('cc'))

#clear- remove full
s1=['aa','bb','cc','cc',123,456,'cc',78.93,56.77]
print(s1)
s1.clear()
print(s1)
del s1
print(s1)




