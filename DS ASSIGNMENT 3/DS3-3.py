#SELECTION BASED ON STRING AND OR OPERATOR
city=input("enter any city name")

if (city=="bangalore") or (city=="delhi"):
	print("selected")
else:
	print("not selected")

#USING AND OPERATOR
city=input("enter any city name")
age=int(input("enter any age"))
exp=int(input("enter experience"))

if (city=="bangalore") and (age<=30) &(exp>=5):
	print("selected")
else:
	print("not selected")

