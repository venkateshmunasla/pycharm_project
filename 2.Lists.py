list1=[1,2,3,4,5,6,7,8,9,1]
print(list1[0])
print(list1[0:5])
print(list1[0:])
print(list1[:5])
print(list1)
list1.append("venkatesh")
print(list1)
print(list1.pop(2))





#pass lists to a functions
#problem==>count the no of even numbers and odd present that list

def count(lists):
    even = 0
    odd = 0
    for i in lists:
        if i%2==0:
            even =even+1
        else:
            odd=odd+1
    return even ,odd
lists=[12,13,14,15,16,17,18,19,20]

even,odd=count(lists)

print("even:{} and odd:{}".format(even,odd))




lists=[2,4,5,7,9,10]
