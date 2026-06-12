class parent:
    property = 90
    
    def eat(self):
        print("parant eating")
        
        
class child(parent):
    property =99
    
    def display(self):
        print("Child class property",self.property)
        print("Parent class property",super().property)
        
    def eat(self):
        print("parent eating")
        
    def calleat(self):
        self.eat()
        super().eat()
        
obj = child()
obj.display()
obj.calleat()
        