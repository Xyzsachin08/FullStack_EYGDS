#single inheritance
'''class dog:
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
class cat(dog):
    def __init__(self, name, age,catid):
        super().__init__(name, age)
        self.catid = catid
        
    def display(self):
        print("Dog name is dobberman"+self.name)
        print("Dog age is"+self.age)
        print("Cat id is"+self.catid)
        
c1 = cat("Sachin","onkar","bhushan")
c1.display()'''


#multilevel Inheritance

'''class dog:
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
class cat(dog):
    def __init__(self, name, age,catid):
        super().__init__(name, age)
        self.catid = catid
        
    def display(self):
        print("Dog name is dobberman"+self.name)
        print("Dog age is"+self.age)
        print("Cat id is"+self.catid)
        
class elephant(cat):
    
   def __init__(self, name, age, catid,weight):
       super().__init__(name, age, catid)
       self.weight = weight
       
   def pillu(self):
        print("Elephant weight is"+self.weight)
        
        
c1 = cat("Sachin","onkar","bhushan")
c1.display()
e1 = elephant(150)
c1.pillu()'''

#multiple Inheritance

class A:
    def math1(self):
        print("Hello from a")
        
class B:
    def math2(self):
        print("Hello from b")
        
class C(A,B):
    def math3(self):
       print("Hello from c")
    
c = C()
c.math1()
c.math2()
c.math3()       

#hybrid inheritance

