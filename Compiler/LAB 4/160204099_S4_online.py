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

fbo_count=0
fbc_count=0
sbo_count=0
sbc_count=0
s="}"
for line in lines:
    index=line.split()
    count=index[0]
    for words in line:
        for alphabet in words:
            if alphabet=="(":
                fbo_count=fbo_count+1
            elif alphabet==")":
                fbc_count=fbc_count+1
                if fbc_count>=2:
                    if fbo_count!=fbo_count:
                        print(") missmatch in line {}".format(count))
            elif alphabet=="{":
                sbo_count=sbo_count+1
            elif alphabet=="}":
                sbc_count=sbc_count+1
                if sbc_count>=2:
                    if sbo_count!=sbc_count:
                        print("{} missmatch in line {}".format(s,count))
