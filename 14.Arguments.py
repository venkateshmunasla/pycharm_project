#positional Arguments
def person(name,age):
    print(name,age)
person("venkatesh",24)

#Keyword Arguments
def person1(name,age):
    print(name)
    print(age)
person1(name="venkatesh",age=24)


#default arguments
#method-1
def person2(name,age=18):
    print(name)
    print(age)
person2(name="venky",age=24)

#method-2#the default arguments always write in last of the arguments
def person3(studentname , rollno,clgname="xyz"):
    return(rollno,studentname,clgname)
a,b,c=person3("venkatesh",100)
print(a ,b, c)


#Variable Length Argument
#problem-1
def person4(a,*b):
    c=a
    for i in b:
        c=c+i
        print(c)
person4(10,3,4,5,6,8,9,10)

#keyword varible length argument ==>note:-(** indiacates the both key and value pairs)
def person5(name,**data):
    print("name=",name)
    for i,j in data.items():
        print(i,":",j)

person5("venkatesh",age=28,city="visakha",job="python developer")





