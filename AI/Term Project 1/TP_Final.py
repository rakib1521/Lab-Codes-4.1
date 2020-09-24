read= open("input.txt","r")
lines=read.readlines()
read.close()
facts=[]
prove=[]
print("INPUT")
for item in lines:
    facts.append(item.replace("\n",""))
    print(item.replace("\n",""))
for line in facts:
    temp_fact=line.split(" | ")
    for l in temp_fact:
        prove.append(l)

print("Graph")
while(len(prove)!=1):
    poped=prove.pop(0)

    if poped[0]=="!":
        item=poped[1:]
        if item in prove:
            print("{} {}".format(poped,item))
            prove.pop(prove.index(item))
        else:
            prove.append(poped)
    else:
        prove.append(poped)
print(prove)
