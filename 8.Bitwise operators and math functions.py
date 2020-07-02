#Bitwise Operators
"""1.Complement(~)
2.and(&)
3.Or(|)
4.XOR(^)
5.LeftShift(<<)
6.Right Shift(>>)"""
#1.complement
a=bin(12)
print(a)

x=~12
print(x)

#2.And(&):
print("and==>",12 & 13)
print("and==>",100 & 300)

#3.OR(|)
print("or==>",12 |13)
print("or==>",100 | 300)

#4.XOR(^)
print("XOR++>",12^13)

#5.leftshift<<
print("leftshift==>",10<<2)

#6.Rightshift>>
print("right shift==>",10>>2)



#Math module
import math
print(math.ceil(12.01))
print(math.floor(12.99999999))

import math as a
list1=[10,20]
print(a.fsum(list1))

from math  import*
import math as b
print(b.fsum(list1))


