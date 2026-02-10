#USE OF OR OPERATOR
#FIND IF ELIGIBLE FOR ADMISSION OR NOT

age=int(input("enter any age"))
avg=int(input("enter average"))
if (age>=18) & (avg>=70):
	print("eligible for admisssion")
else:
	print("not eligible for admission")


#USE OF | OPERATOR
avg=int(input("enter average marks"))
if (avg>=70)or(avg<=80):
	print("eligible for admission")
else:
	print("not eligible for admission")
