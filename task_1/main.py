####### Task-1########
class Car:
    print("-----Welcome to the Car Info!------")
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color
    def display_info(self):
        print(f"Brand is {self.brand} and color is {self.color}")
car = Car("Toyota","Black")
car1=Car("Honda","White")
#call the class method
car.display_info()
car1.display_info()