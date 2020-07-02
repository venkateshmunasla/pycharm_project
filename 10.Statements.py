#if
x=10
y=20
z=30
s=10
if x<y:
    print ("True")

#if -else
if x==y:
    print("true")
else:
    print("false")


#el-if
if y%x!=0:
    print("the reminder is not zero")
elif y%x==0:
    print("the reminder is zero")
else:
    print("the y value is prime number")



#nested if
if x+y==z:
    print("z=30")
    if y-x==s:
        print("s=10")
        if y/x==2:
            print("divider is 2")
        else:
            print("divider is not 2")
    else:
        print("s value is not equal to y-x")
else:
    print("z value is not equal to x+y")