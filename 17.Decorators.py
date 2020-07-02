#Actual function
def men(name,age):
    print("my name is",name)
    print("my age is",age)
m=men("venkatesh",24)


#decorators==>(the actual didnt change the name and age directly with the help of decorator function)
def men(name,age):
    print("my name is",name)
    print("my age is",age)

def men_modify(func): #this func is a men function
    def inner_modify(name,age):
        if len(name)>=9 and age>=18:
            print("the person name should be contain at more then 9 characters")
            print("the age should be above age 18")
        return func(name,age)  #the func is men function passing the men function values
    return inner_modify
men=men_modify(men)
names=input("pls enter the name:")
ages=int(input("pls enter the age:"))
men(names,ages)





m=men("venkatesh",24)
