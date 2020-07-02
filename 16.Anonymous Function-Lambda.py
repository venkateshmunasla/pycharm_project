#Anonymous function(The function calling without name is callling anonymous function)
#problem-1
f=lambda a:a*a
result=f(5)
print(result)

#problem-2
f1=lambda a,b:a*b
result1=f1(10,20)
print(result1)

#Filters
#method-1(with out using lambda function)
def is_even(n):
    return n%2==0
nums=[1,2,3,4,5,6,7,8,9]
a=list(filter(is_even,nums))
print(a)

#method-2(with using lambada function)
nums=[1,2,3,4,5,6,7,8,9]
a=list(filter(lambda n:n%2==0,nums))
print(a)

#Map function
nums=[1,2,3,4,5,6,7,8,9]
a=list(filter(lambda n:n%2==0,nums))
print(a)
b=list(map(lambda x:x*x,a))
print(b)

#Reduce function
nums=[1,2,3,4,5,6,7,8,9]
a=list(filter(lambda n:n%2==0,nums))
print(a)

b=list(map(lambda x:x*x,a))
print(b)
from functools import*

c=reduce(lambda a,b:a+b,b)
print(c)



