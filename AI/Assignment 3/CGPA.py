#taking input to write in the file
f1=open("test.py", "w")
print("\n")
for i in range(3):
        name=str(input("Enter the name:"))
        dept=str(input("Enter the department:"))
        cgpa=str(input("Enter the cgpa:"))
        std=name+"\t"+dept+"\t"+cgpa
        print(std, end="\n", file=f1)
        print("\n")
f1.close

#reading from a file to dictionary
f1 = open("test.py", "r")
dict = {}
for l in f1:
    list = []
    name, dept, cgpa =l.split("\t")
    cgpa = cgpa.replace('\n','')
    list.append(dept)
    list.append(cgpa)
    (key , val) = name , list
    dict[key] = val

print(dict)

#changing  cgpa and writing back to file
f1=open("test.py", "w")
print("\n")
for key,value in dict.items():

    value[1] = 4.0
    name = str(key)
    dept = str(value[0])
    cgpa = str(value[1])
    std = name + "\t" + dept + "\t" + cgpa
    print(std, end="\n", file=f1)
    print("\n")

f1.close

# after change reading from a file to dictionary
f1 = open("test.py", "r")
dict = {}
for l in f1:
    list = []
    name, dept, cgpa =l.split("\t")
    cgpa = cgpa.replace('\n','')
    list.append(dept)
    list.append(cgpa)
    (key , val) = name , list
    dict[key] = val

print(dict)
