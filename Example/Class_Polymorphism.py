#polymorphism
class BMW(): 
     def type(self): 
       print("BMW M5") 
     def color(self):
       print("Black") 
class Audi(): 
     def type(self): 
       print("Audi RS6") 
     def color(self): 
       print("Black") 
#create a function called “func()” which will take an object which we will name “obj”
def func(obj): 
       obj.type() 
       obj.color()
#call the methods type() and color(), each of which is defined in the two classes
car_a = BMW() 
car_b = Audi() 
func(car_a) 
print(end="\n")
func(car_b)