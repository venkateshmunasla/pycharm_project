#numerical data types
a=10
b=20
print(type(a))
print(int(a))#int
print(float(a))#float
print(complex(a,b))#complex
print(a<b)#boolean

#sequence data types
'''1.Lists
2.Tuples
3.Sets
4.Strings
5.range
6.dictionaries'''

#range function converted into list
Ra=range(0,100)
print(Ra)
k=[*range(1,10)]   #note:- We can use argument-unpacking operator
print(k)


#we can use extend() function to unpack the result of range
mylist=[]
start,end=10,30
if start <end:
    mylist.extend(range(start,end))

print(mylist)



mylist=[]
start,end=10,30
if start <end:
    mylist.extend(range(start,end,2))

print(mylist)


