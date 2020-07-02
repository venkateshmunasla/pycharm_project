#Recursion
import sys
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())

i=1
def greet():
    global i
    i=i+1
    print("hello",i)
    greet()
greet()

#Recursion with factroail
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
result=fact(5)
print(result)