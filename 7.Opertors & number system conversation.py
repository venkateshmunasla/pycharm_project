#1.Arthemitical operator

a=10
b=20
print(a+b , a-b ,a/b ,a//b, a*b)


#Assignment operators
k=100
l=k
print(l,k)

#value adding it self
k +=5  # or k=k+5
print(k)

# values assiging in same line
x,y=100,200
print(x,y)

#3.unary opertors(to sign negative sign)
n=7
print(n)
print(-n)


#4.Relational Operators
a1=5
b1=10
print(a1<b1)
print(a1>b1)
print(a1<=b1)
print(a1>=b1)
print(a1==b1)
print(a1!=b1)

#5.Loical OPerators
r=10
s=100

#AND
print("and==>",r<100 and s<=100)
print("and==>",r<1 and s<=100)

#OR
print("or==>",r<1 or s<=10)
print("or==>",r<1 or s<=100)
print("or==>",r<100 or s<=100)

#NOT (Reverse the out put)

print ("not==>",not(r<=10 and s<=100))



#number system conversition
v=100
print("int==>",int(v))
print("int to bin==>",bin(v))
print("bin to int==>",int(0b1100100))
print("int to oct==>",oct(v))
print("int to hex==>",hex(v))
print()

#swap to numbers
#method-1
a=100
b=200
a,b=b,a
print(a,b)

#method-2
c=500
d=100
temp=c
c=d
d=temp
print(c,d)