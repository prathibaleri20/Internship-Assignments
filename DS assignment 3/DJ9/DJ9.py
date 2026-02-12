s1={"tally","oracle","java","python","vba","autocad"}
print(s1)

#printing using for loop
s1={"tally","oracle","java","python","vba","autocad"}
for i in s1:
	print(i)

#type display
s1={"tally","oracle","java","python","vba","autocad"}
print(type(s1))

#converting the set data into list data
s1={"tally","oracle","java","python","vba","autocad"}
print(s1)
s2=(["tally","oracle","java","python","vba","autocad"])
print(s2)
s1={"tally","oracle","java","python","vba","autocad"}
print(s1)
s1.add("networking")
print(s1)

#add to set and using for loop
s1={"tally","oracle","java","python","vba","autocad"}
print(s1)
s1.add("networking")
for i in s1:
	print(i)

#To add more than one item in the set, Python provides the update() method.--USING SET()
s1=set(['tally','oracle','java','python','vba','autocad'])
print(s1)
s1.update(['networking','ccna','mcse','aws'])
print(s1)

#To add more than one item in the set, Python provides the update() method--DIRECTLY INTO THE SET
s1={'tally','oracle','java','python','vba','autocad'}
print(s1)
s1.update(['networking','ccna','mcse','aws'])
print(s1)

#Removing items from the set--ONLY ONE DATA AT TIME
#discard()
s1={'tally','oracle','java','python','vba','autocad'}
print(s1)
s1.discard('oracle')
print(s1)

s1={'tally','oracle','java','python','vba','autocad'}
print(s1)
s1.pop()
print(s1)

#clear()
s1={'tally','oracle','java','python','vba','autocad'}
print(s1)
s1.clear()
print(s1)

#use of union()
s1={'tally','oracle','java','python','vba','autocad'}
print(s1)
s2={'python','vba','autocad'}
print(s1.union(s2))

s1={'tally','oracle','java','python','vba','autocad'}
print(s1)
s2={'python','vba','autocad'}
print(s1|s2)
print(s1&s2)

#intersection
s1={'tally','oracle','java','python','vba','autocad'}
print(s1)
s2={'python','vba','autocad'}
print(s1.intersection(s2))

#difference
s1={'tally','oracle','java','python','vba','autocad'}
s2={'python','vba','autocad'}
print(s1-s2)
print(s1.difference(s2))

