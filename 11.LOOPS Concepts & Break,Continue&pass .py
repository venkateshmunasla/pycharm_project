#While loop

a=1
while a<=10:
    print("my name is venkatesh")
    a+= 1;


#Nested loop
a=1
while a<=5:
    print(a)
    b=1
    while b<=5:
        print("i love india",end=" .")
        b+=1
    a+=1
    print()



#for loop
a=-1
for i in range(10):
    print(i)
    a=a+1
    print("value of a is",a)


#For Loop else
nums=[12,14,16,17,19]
for i in nums:
    if i %5==0:
        print(i)
else:
    print("not found .nums list any number did not divisibe by 5 ")



#Break
av=5
s=1
while s<=10:
    if s>av:
        break
    print("i love my country")
    s+=1

print("loop close at",s)


#continue
j=0
for i in range(1,11):
    j=j+i
    if j>=100:
        continue
    print(j)

#Pass
for i in range (1,10):
    if i%2!=0:
        pass
    else:
        print(i)
print("byee")
