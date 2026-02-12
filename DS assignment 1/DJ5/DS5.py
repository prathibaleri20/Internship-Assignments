
#print from 1 -10
for i in range(1,10):
	print(i)

#FOR PRINTING NUMBERS FROM 1 - 10 , WE HAVE TO SPECIFY 1 - 11 IN THE FOR LOOP

for i in range(1,11):
	print(i)

#PRINTING EVEN NUMBERS FROM 20 - 50 with gap of 2 numbers

for i in range(20,51,2):
	print(i)


#printing odd numbers
for i range(19,51,2):
	print(i)


#printing multiples of 5 till 50
for i in range(5,51,5):
	print(i)

#printing multiples of 10 till 100
for x in range(10,110,10):
	print(x)

#printing numbers from 10 - 1 --> descending order
for x in range(10,1,-1):
	print(x)

#printing even numbers from 50 - 20 in reverse order
for x in range(50,21,-2):
	print(x)

#printing multiples of 5 from 50 - 5 in reverse order
for x in range(50,0,-5):
	print(x)

#printing multiples of 10 from 100 - 10 in reverse order
for x in range(100,0,-10):
	print(x)

#printing names 10 times

for i in range(1,11):
	print("Prathiksha")

#printing name with serial number
for i in range(1,11):
	print(i,"Prathiksha")

#printing any name with serial number
name=input("enter any name")
for i in range(1,11):
	print(i,"     ",name)

#While loop
i=1
while(i<=10):
	print(i)
	i=i+1

i=5
while(i<=50):
	print(i)
	i=i+5


i=10
while(i<=100):
	print(i)
	i=i+10

i=50
while(i>=20):
	print(i)
	i=i-2

i=10
while(i>=1):
	print(i)
	i=i-1

for i in range(10):
    print(i,end = ' ')


n = int(input("Enter the number "))
for i in range(1,11):
    c = n*i
    print(n,"*",i,"=",c)


for i in range(2,n,2):
    print(i)


for i in range(0,5):
    print(i)
else:
    print("for loop completely exhausted, since there is no break.")


# Iterating string using for loop
str = "Python"
for i in str:
    print(i)








































