#DICTIONARY IN PYTHON
d1={101:"pooja",102:"sanjay",103:"harshitha"}
#HERE WE CAN SEE THE KEY-VALUE PAIRS
#KEYS SHOULD BE UNIQUE
print(d1)

s1={1:'tally',2:'oracle',3:'java',4:'python',5:'vba',6:'autocad'}
print(s1)

#Updating Dictionary
s1={1:'tally',2:'oracle',3:'java',4:'python',5:'vba',6:'autocad'}
print(s1)
s1[1]='networking'
print(s1)
s1[5]='MD'
print(s1)

#remove entry with key(Deleting the Data from the Dictionary)
s1={1:'networking',2:'oracle',3:'java',4:'python',5:'vba',6:'autocad'}
print(s1)
del s1[1]
print(s1)

#remove all entries(deletes only the data, NOT the dictionary)
s1={1:'tally',2:'oracle',3:'java',4:'python',5:'vba',6:'autocad'}
print(s1)
s1.clear()
print(s1)

#delete entire dictionary(deletes both the data and the dictionary)
s1={1:'tally',2:'oracle',3:'java',4:'python',5:'vba',6:'autocad'}
print(s1)
del s1
#print(s1)
#THIS THROWS AN ERROR SAYING NOT AVAILABLE

#SLICING CANNOT BE DONE IN DICTIONARY
#BUT IT IS POSSIBLE ONLY IN LISTS

#FIND LENGTH
s1={1:'tally',2:'oracle',3:'java',4:'python',5:'VBA',6:'CN'}
print(s1)
print(len(s1))


s1={1:'tally',2:'oracle',3:'java',4:'python',5:'vba',6:'CN'}
print(s1)
x=len(s1)
print(x)

#copying data
s1={1:'tally',2:'oracle',3:'java',4:'python',5:'vba',6:'autocad'}
print(s1)
s2=s1.copy()
print(s2)


#USING get()
s1={1:'tally',2:'oracle',3:'java',4:'python',5:'vba',6:'autocad'}
print(s1)
print(s1.get(3))
print(s1[3])


#USING values() & items()
s1={1:'tally',2:'oracle',3:'java',4:'python',5:'vba',6:'autocad'}
print(s1)
print(s1.items())


s1={1:'tally',2:'oracle',3:'java',4:'python',5:'vba',6:'autocad'}
print(s1)
print(s1.values())


# keys() to get the unique keys
print(s1.keys())

s1={1:'tally',2:'oracle',3:'java',4:'python',5:'vba',6:'autocad'}
print(s1)
print(len(s1.keys()))

#Another method to display the data of the dictionary data --USING "for" loop
s1={1:'tally',2:'oracle',3:'java',4:'python',5:'vba',6:'autocad'}
print(s1)
for i in s1:
	print(s1.get(i))

#concatenate or merging 2 dictionaries
s1={1:'tally',2:'oracle',3:'java',4:'python',5:'vba',6:'autocad'}
print(s1)
s2={7:'networking',8:'cn',9:'cyber security'}
print(s2)
s3=s1.update(s2)
print(s1)

#converting all dictionary data to List
s1={1:'tally',2:'oracle',3:'java',4:'python',5:'vba',6:'autocad'}
print(s1)
x1=list(s1.values())
print(x1)

#converting all dictionary data to Tuple
s1={1:'tally',2:'oracle',3:'java',4:'python',5:'vba',6:'autocad'}
print(s1)
x1=tuple(s1.values())
print(x1)





















































