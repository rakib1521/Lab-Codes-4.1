i=0
f=False

def F():
    global i
    global f
    if x[i].isdigit():
        i=i+1
        f=True
        return
    elif x[i]=="a" or x[i]=='b' or x[i]=='c' or x[i]=='d' or x[i]=='e':
        i=i+1
        f=True
        return
    elif x[i]=='(':
        i=i+1
        E()
        i=i+1
        if x[i]==')':
            f=True
            return



def T():
    global i
    global f
    F()
    if i <len(x)-1:
        if x[i]=="*" or x[i]=="/":
            i=i+1
            F()
        elif f==True:
            return


def E():
    global i
    global f
    T()
    if i <len(x)-1:
        if x[i]=="+" or x[i]=="-":
            i=i+1
            T()
        elif f==True:
            return





print("CFG")
print("E -> T + T | T - T | T")
print("T -> F * F | F / F | F")
print("F -> (E) | ID | NUM")
print("ID -> a|b|c|d|e")
print("NUM -> 0|1|2|...|9")
x = input("Enter string ")

if len(x)>=1:
    E()
else:
    print("Invalid")
if len(x)==i and f==True:
    print("valid")
else:
    print("Invalid")
