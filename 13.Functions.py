#Print Function-1 with values
def vinayaka():
    a=100
    b=200
    print(a+b)
vinayaka()


#print Function-2 the values given by user
def vinayaka1(a,b):
     print(a+b)
vinayaka1(10,20)



#Return Function-1 with values
def vinayakaya():
    a=100
    b=900
    return a+b
a=vinayakaya()
print(a)

#Return function-2.the values given by user
#method-1
def vinayakaya1(a,b,c):
    return a+(b*c)
ve=vinayakaya1(10,20,5)
print(ve)

#method-2
def vinayakaya1(a,b,c):
    x=a+b+c
    y=a*b*c
    z=a/b/c
    return x,y,z
ve,nk,at=vinayakaya1(10,20,5)
print(ve ,nk ,at)















