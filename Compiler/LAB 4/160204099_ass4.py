read= open("input.c")
lines=read.readlines()
read.close()
write=open("output1.txt","w")
count=1
for line in lines:
        write.writelines("{} {}".format(count,line))
        count=count+1
write.close()
read= open("output1.txt")
lines=read.readlines()
read.close()
write=open("output2.txt","w")
for line in lines:
    index=line.split()
    count=index[0]
    if "/*"  in index:
        write.writelines("{}\n".format(count))
    elif "//"  in index:
        write.writelines("{}\n".format(count))

    else:
        li=line.split()
        sen=" ".join(li)
        write.writelines("{}\n".format(sen))
write.close()
read= open("output2.txt")
lines=read.readlines()
read.close()
####
b=["{","}","(",")","=",";","<",">",",","+","-","*","/"]
write=open("output.txt","w")


string=''
for line in lines:
    #if len(line.split())==1:
        #write.writelines("{}".format(line))

    for words in line:
        for alphabet in words:
            if alphabet in b:

                string+=" "+str(alphabet)+" "

            else:
                string+=str(alphabet)

write.writelines("{}\n".format(string))


write.close()

####

####
name=["int","float","double","return",'if','else',"","void"]
read= open("output.txt")
lines=read.readlines()
read.close()
write=open("output.txt","w")
temp_item=" "
string2='id'
string=''
count=0
for line in lines:
    id=line.split(" ")
    #print(id)
    temp_item=" "
    for item in id:
        count=count+1
        if item not in name and item[0].isalpha()==True and item!=temp_item:
            #if count>9:
                #temp_index=id.index(item)
                #temp_index=temp_index*10

            #else:
            temp_index=id.index(item)
            id.insert(temp_index,string2)
            temp_item=item
            #print(id)
            #break
            #print(temp_index)
            #print(item)

    string=" ".join(id)
    #print("STRING : {}".format(string))
    write.writelines("{}".format(string))


write.close()

####

def duplicate_token(li,count):
    b=[";",","]
    b_0=0
    b_1=0
    for item in li:
        if item==b[0] :
            b_0=b_0+1
            if b_0>=2:
                print("{} missmatch in line {}".format(b[0],count))
                break;
        else:
            if b_0>0:
                b_0=b_0-1

def duplicate_dtype(li,count):
    b=["float","double","int"]
    b_0=0

    for i in range(len(b)):
        for item in li:
            if item==b[i] :
                b_0=b_0+1
                if b_0>=2:
                    print("{} missmatch in line {}".format(b[i],count))
                    break;
            else:
                if b_0>0:
                    b_0=b_0-1
    b_0=0


##########
read= open("output.txt")
lines=read.readlines()
read.close()

for line in lines:
    print(line)

count=0
fbo_count=0
fbc_count=0
sbo_count=0
sbc_count=0
if_count=0
else_count=0
s="}"
for line in lines:
    index=line.split()
    #print(index)
    count=count+1
    duplicate_token(index,count)
    duplicate_dtype(index,count)
    for words in index:

            if words=="(":
                fbo_count=fbo_count+1
            elif words==")":
                fbc_count=fbc_count+1
                if fbc_count>=2:
                    if fbo_count!=fbo_count:
                        print(") missmatch in line {}".format(count))
            elif words=="{":
                sbo_count=sbo_count+1
            elif words=="}":
                sbc_count=sbc_count+1
                if sbc_count>=2:
                    if sbo_count!=sbc_count:
                        print("{} missmatch in line {}".format(s,count))
            elif words=="if":
                if_count=if_count+1
            elif words=="else":
                else_count=else_count+1
                if else_count>=2:
                    if if_count!=else_count:
                        print("else missmatch in line {}".format(count))
