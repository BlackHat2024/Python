#cass inheritance
#declare class car with brand and type arguments
class Car:
  def __init__(self, mark, model):
    self.brnd = mark
    self.type = model
#declare a class year that extends class car
class Year(Car):
    def __init__(self, mark, model, year):
        super().__init__(mark, model)
        self.pyear = year

#sample input provided
x = Year("BMW", "M5", 2022)
#printing the result 
print("Brand : {} \nModel: {} \nYear: {}".format(x.brnd,x.type,x.pyear))