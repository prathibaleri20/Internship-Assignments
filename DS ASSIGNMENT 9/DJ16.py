# both activities -- write and read
f1 = open(r"C:\Users\HP\Downloads\sample.txt", "w")
f1.write("first line sample data\n")
f1.write("second line sample data\n")
f1.close()

f1 = open(r"C:\Users\HP\Downloads\sample.txt", "r")
print(f1.read())


# working with "append" mode
f1 = open(r"C:\Users\HP\Downloads\sample.txt", "a")
f1.write("third line sample data\n")
f1.write("fourth line sample data\n")
f1.close()

f1 = open(r"C:\Users\HP\Downloads\sample.txt", "r")
print(f1.read())


# using "with" keyword
with open(r"C:\Users\HP\Downloads\sample.txt", "w") as f1:
    f1.write("hello python")

with open(r"C:\Users\HP\Downloads\sample.txt", "r") as f2:
    print(f2.read())


# with command + append
with open(r"C:\Users\HP\Downloads\sample.txt", "a") as f1:
    f1.write("hello oracle")

with open(r"C:\Users\HP\Downloads\sample.txt", "r") as f2:
    print(f2.read())


# split() -- function
with open(r"C:\Users\HP\Downloads\sample.txt", "r") as f2:
    data = f2.readlines()
    for x in data:
        print(x.split())


# THE LAST LINE SPLIT EACH AND EVERY LINE INTO A LIST
with open(r"C:\Users\HP\Downloads\sample.txt", "r") as f2:
    data = f2.readlines()
    for x in data:
        print(x.split())

# WE CAN ALSO STORE EACH LIST INTO A VARIABLE AND PRINT IT INDIVIDUALLY
with open(r"C:\Users\HP\Downloads\sample.txt", "r") as f2:
    data = f2.readlines()
    for x in data:
        a1 = x.split()
print(a1)