a=10
b=10
print(id(a) , type(a))
print(id(b), type(b))


#local variables

def func():
    a=10   #inside of the class define the variable is called local varible
    print(a)
func()



#Global variable
b=100  #a varible define as the out side of the is called global variable
def func1():
    print(b)
func1()

#The global varible call into the function and change the global varible value
a=10
def func2():
    global a
    a=15
    print("inner function",a)
func2()
print("out function",a)

##The global varibles call into the functionchange the global varible value

a=10
print(id(a))
b=20
print(id(b))
c=30
print(id(c))
def func3():
    a=1234
    x=globals()["a"]
    y=globals()["b"]
    z=globals()["c"]
    print("local variable value",a)
    print("call the global varible value into function",x)
    print("call the global varible value into function", b)
    print("call the global varible value into function", z)

    print(id(x))
    print(id(y))
    print(id(z))
    x = globals()["a"]=100
    y = globals()["b"]=200
    z = globals()["c"]=300
    print("changing a global varibale value",a)
    print("changing a global varibale valuez",b)
    print("changing a global varibale value",c)
    print(id(x))

    print(x)
func3()
print("changing a global varibale value call the outside of the function",a)
print("changing a global varibale valuez call the outside of the function",b)
print("changing a global varibale value call the outside of the function",c)