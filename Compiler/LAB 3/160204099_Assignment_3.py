li=[]
#read from file
with open('input.txt','r') as file:
    for line in file:
        for word in line.split("] "):
            word=word+"]"
            li.append(word)

last_item=li.pop()

li.append(last_item[:-1])


print("Step 1")
print(li)

#remove keyword
new_list=[]
for item in li:
    if item[1:3]=="id":

        new_list.append(item)
    else :
        holder=item.split()
        var="["+holder[1]

        new_list.append(var)

print("Step 2")
print(new_list)
final_list=[]

for item in new_list:
    #print(item)
    final_list.append(item[1:-1])
#print(final_list)








#sore every variable in dict and list
def store(sl_no,name,id_type,data_type,scope,value):
    #print(value)

    dict={
            'sl_no':sl_no,
            'name':name,
            'id_type':id_type,
            'data_type':data_type,
            'scope':scope,
            'value':value

        }
    table_list_list.append([sl_no,name,id_type,data_type,scope,value])
    scope='global'
    id_type='var'
    value=0
    data_type=''
    #print(table_list_list)
    table_list.append(dict)

def insert():
    #print(final_list)
    data_type_flag=False
    sl_no=1
    data_type_demo=['int','float','double']
    scope='global'
    id_type='var'
    value=0
    data_type=''
    name=""
    value_flag=False
    name_flag=False
    data_type_flag=False
    func_name=""
    first_bracket_flag=False
    second_bracket_flag=False

    temp_value_flag=False
    temp_name_flag=False
    temp_data_type_flag=False
    temp_scope=""
    temp_printed=True
    for item in final_list:
        #print(item)

        if item in data_type_demo and data_type_flag==False and first_bracket_flag==False and second_bracket_flag==False:
            data_type=item
            data_type_flag=True
        elif item[0:2]=='id' and name_flag==False and first_bracket_flag==False and second_bracket_flag==False:
            holder=item.split()
            name=holder[1]
            name_flag=True
        elif item=="=" and value_flag==False and first_bracket_flag==False and second_bracket_flag==False:
            value_flag=True
        elif item !="=" and value_flag==True and first_bracket_flag==False and second_bracket_flag==False:
            value=item
            #print("printing from normal")
            store(sl_no,name,id_type,data_type,scope,value)
            name_flag=False
            data_type_flag=False
            value_flag=False
            value=0
            sl_no=sl_no+1


    ####

        elif item=="(" and first_bracket_flag==False and second_bracket_flag==False:
            first_bracket_flag=True
            if first_bracket_flag==True:
                temp_name=name
                id_type='func'
                #print("printing from (")
                store(sl_no,name,id_type,data_type,scope,value)
                sl_no=sl_no+1
                value=0
                name_flag=False
                data_type_flag=False
                value_flag=False
                temp_scope=temp_name
                scope=temp_scope
                id_type='var'
    #####
        elif item in data_type_demo and temp_data_type_flag==False and first_bracket_flag==True and second_bracket_flag==False:
                data_type=item
                temp_data_type_flag=True
        elif item[0:2]=='id' and temp_name_flag==False and first_bracket_flag==True and second_bracket_flag==False:
                holder=item.split()
                name=holder[1]
                temp_name_flag=True
        elif item=="=" and temp_value_flag==False and first_bracket_flag==True and second_bracket_flag==False:
                temp_value_flag=True
        elif item !="=" and temp_value_flag==True and first_bracket_flag==True and second_bracket_flag==False:
                value=item
                temp_value_flag=False
    ####

        elif item==")" and first_bracket_flag==True and temp_data_type_flag==True and second_bracket_flag==False:
                #print("printing from )")
                store(sl_no,name,id_type,data_type,temp_scope,value)
                sl_no=sl_no+1
                value=0
                temp_name_flag=False
                temp_data_type_flag=False
                temp_value_flag=False
                first_bracket_flag=False
        elif item==")" and first_bracket_flag==True :
                temp_name_flag=False
                temp_data_type_flag=False
                temp_value_flag=False
                first_bracket_flag=False

    ####

    ####

        elif item=="{" and second_bracket_flag==False:
                    second_bracket_flag=True

    #####
        elif item in data_type_demo and temp_data_type_flag==False and first_bracket_flag==False and second_bracket_flag==True:
            #print(item)
            data_type=item
            temp_data_type_flag=True
        elif item[0:2]=='id' and temp_name_flag==False and first_bracket_flag==False and second_bracket_flag==True:
            holder=item.split()
            name=holder[1]
            #print(name)
            temp_name_flag=True
        elif item=="=" and temp_value_flag==False and first_bracket_flag==False and second_bracket_flag==True:
            temp_value_flag=True
        elif item !="=" and temp_value_flag==True and first_bracket_flag==False and second_bracket_flag==True:
            value=item
            #print(value)
            temp_printed=False
        if (temp_name_flag==True and temp_data_type_flag==True and temp_value_flag==True and temp_printed==False)  and first_bracket_flag==False and second_bracket_flag==True:
            #print("printing from {")
            store(sl_no,name,id_type,data_type,temp_scope,value)
            sl_no=sl_no+1
            temp_name_flag=False
            temp_data_type_flag=False
            temp_value_flag=False
            value=0
            temp_printed=True
    ####

        elif item=="}" and second_bracket_flag==True:
                 second_bracket_flag=False
                 scope='global'

    ####

        #print(table_list_list)
        #return table_list_list
    select()
def display():
    if not table_list_list:
        print("Please Insert First")
    else:
        label_list=["Sl. No","Name","Id Type","DType","Scope","Value"]
        for i in label_list:
            print(i,end='\t')
        print(end='\n')
        for item in table_list_list:
            for i in item:
                print(i,end='\t')
            print(end='\n')
    select()
def delete():
    if not table_list_list:
        print("Please Insert First")
    else:
        label_list=["Sl. No","Name","Id Type","DType","Scope","Value"]
        for i in label_list:
            print(i,end='\t')
        print(end='\n')
        for item in table_list_list:
            if item[4]=='global':
                for i in item:
                    print(i,end='\t')
                print(end='\n')
        select()


def select():
    print("1.Insert")
    print("2.Delete")
    print("3.display")
    print("4.exit")

    select=int(input("Enter the Number:"))
    op_list=[]
    if select==1:
        op_list=insert()
        #print(op_list)
    elif select==2:
        delete()
    elif select==3:
        display()
    elif select==4:
        quit()


table_list=[]


table_list_list=[]

select()
