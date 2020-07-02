#Constuctor
class venky:
    pass
v1=venky()
v2=venky()
print(id(v1))
print(id(v2))    #note:- if u run code again the adress of object changes every code execution time

#self
class person:
    def __init__(self):
        self.name="venky"
        self.age=24
p1=person()
p2=person()
p1.age=18
p2.name="ramesh"
print("change init variables==>","name=",p1.name,"age=",p1.age)

#comprassion of objects
#problem-1
class person1:
    def __init__(self):
        self.name="jhony"
        self.age=30
    def compare(self,others):
        if self.age==others.age:
           return True
        else:
            return False

#problem-2
class person2:
    def __init__(self):
        self.car="audi"
        self.modelno="12345"
    def update(self):
        self.car="benz"
        self.modelno
        print(self.car,self.modelno)
z1=person2()
z1.update()

#Comprassion
class  computre:
    def __init__(self):
        self.name="venky"
        self.age="24"
    def compare(self,other):
        if self.age==other.age:
            return True
        else:
            return False
c1=computre()
c1.age=30
c2=computre()
if c1.compare(c2):
    print("they are same")
else:
    print("they are different")
print(c1.name)
print(c2.name)





















