i=0
f=False

def loop_stat():
    global i
    global f

    if(x[i:i+5]=="while"):
        i=i+5

        if x[i]=="(":
            i=i+1

            expn()
            #i=i+1

            if x[i]==')':
                i=i+1

                start()
                if i==len(x):
                    return
                else:

                    f=False
                    return
            else:

                return
        else:

            f=False
            return


    if(x[i:i+3]=="for"):
        i=i+3

        if x[i]=="(":
            i=i+1


            asgn_stat()
            if x[i]==";":
                i=i+1
                expn()
                i=i+1
                if x[i]==";":

                    i=i+1
                    asgn_stat()

                    if x[i]==")":
                        i=i+1

                        start()
                        if(i==len(x)):

                            return
                        else:

                            f=False
                            return
                    else:

                        f=False
                        return
                else:

                    f=False
                    return
            else:

                f=False
                return
        else:

            f=False
            return



def extn1():
    global i
    global f
    if (len(x)-1)==i:
        f=True
        i=i+1
        return
    elif(x[i:i+3]=="else"):
        i=i+4
        f=False
        start()
        if(f==True):
            return
        else:
            f=False
            return
    else:
        f=False
        return


def dscn_stat():
    global i
    global f
    if x[i]=='i':
        i=i+1
    if x[i]=="f" and x[i-1]=="i":
        i=i+1
    if x[i]=="(":
        i=i+1

        expn()
        if x[i]==")":
            i=i+1
            start()
            if i ==len(x):
                return
            else:
                if f==True:
                    extn1()
                else:
                    return
    else:
        f=False
        return

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

def smpl_expn():
    E()
    if f==True and i==len(x):
        return
    else:
        return


def relop():
    global i
    global f
    if x[i]=="=":
        i=i+1
        if x[i]=='=':
            f=True
            return
        else:
            f=False
            return
    elif x[i]=="!":
        i=i+1
        if x[i]=='=':
            f=True
            return
        else:
            f=False
            return
    elif x[i]=="<":
        i=i+1
        f=True
        if x[i]=='=':
            f=True
            return
        else:
            f=False
            return
    elif x[i]==">":
        i=i+1
        f=True
        if x[i]=='=':
            i=i+1
            f=True
            return
        else:
            f=False
            return
    elif x[i]==">":
            i=i+1
            f=True
            return
    elif x[i]=="<":
            i=i+1
            f=True
            return
    else:
        f=False
        return





def extn():
    global i
    global f
    if len(x)-1==i:
        f=True
        i=i+1
        return
    else:
        relop()
        if f==True:
            smpl_expn()
            if(len(x)==i):
                return
            else:
                return


def expn():
    global i
    global f
    smpl_expn()
    if len(x)==i:
        return
    else:
        if f==True:
            extn()
            return

def asgn_stat():
    global i
    global f
    if x[i]=="a" or x[i]=='b' or x[i]=='c' or x[i]=='d' or x[i]=='e':

        i=i+1
        if x[i]=='=':

            i=i+1
            expn()
            if f==True and i==len(x):
                return
            else:
                f=True
                return
    else:
        f=False
        return


def start():
    global i
    global f
    s_f=False
    asgn_stat()
    s_f=True
    if f==True and len(x)==i:
        return
    elif f==True:
        return
    if s_f==True and f==False:

        dscn_stat()
        if f==False:

            loop_stat()



print("CFG")
print("<stat> -> <asgn_stat> | <dscn_stat> | <loop_stat>")
print("<asgn_stat> -> id = <expn>")
print( "<expn> -> <smpl_expn> <extn>")
print("<extn> -> <relop> <smpl_expn> | epsilon")
print("<dcsn_stat> -> if (<expn> ) <stat> <extn1>")
print("<extn1> -> else <stat> | epsilon ")
print("<loop_stat> -> while (<expn>) <stat> | for (<asgn_stat> ; <expn> ; <asgn_stat> ) <stat>")
print("<relop> -> == | != | <= | >= | >| <")
x = input("Enter string ")

if len(x)>=1:
    start()
else:
    print("Invalid")
if len(x)==i and f==True:
    print("valid")
else:
    print("Invalid ")
