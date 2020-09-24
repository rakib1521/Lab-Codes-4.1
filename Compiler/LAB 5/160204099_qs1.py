i=0
f=False
def X():
    global i
    global f
    if len(x)-1 ==i:
        f=True
        return
    else:
        if x[i]=='b':
            i=i+1
            if x[i]=='b' or x[i]=='c':
                i=i+1
                X()
            else:
                f=False
                return

def A():
    global i
    global f
    if(x[i]=='a'):
        i=i+1
        X()
        if f==True and x[i]=='d':
            i=i+1
            f=True
            return

print("CFG")
print("A -> aXd")
print("X -> bbX | bcX | epsilon")


x = input("Enter string ")

if len(x)>=1:
    A()
else:
    print("Invalid")
if len(x)==i and f==True:
    print("valid")
else:
    print("Invalid")
