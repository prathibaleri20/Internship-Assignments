f1 = open(r'C:\Users\HP\Downloads\programs.txt', 'r')
for each in f1:
    print(each)

f1 = open(r'C:\Users\HP\Downloads\programs.txt', 'r')
print(f1.read())

f1 = open(r'C:\Users\HP\Downloads\programs.txt', 'r')
print(f1.read(10))


f1 = open(r'C:\Users\HP\Downloads\programs.txt', 'w')
f1.write("this is second line into the same file")
f1.close()


f1 = open(r'C:\Users\HP\Downloads\programs.txt', 'w')
f1.write("sample data to store into the file \n")
f1.write("this is second line into the same file")
f1.close()

