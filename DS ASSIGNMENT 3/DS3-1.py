#uSE OF AND OPERATOR

#CHECK IF ELIGIBLE FOR ADMISSION

age=int(input("enter any age"))
avg=int(input("enter average"))

if (age>=18) and (avg>=70):
	print("eligible for admisssion")
else:
	print("not eligible for admission")

# USE OF &
age=int(input("enter any age"))
avg=int(input("enter average"))

if (age>=18) & (avg>=70):
	print("eligible for admisssion")
else:
	print("not eligible for admission")
