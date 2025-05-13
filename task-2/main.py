##### Task-2#######
class Calculator: # class aik blue print hoti h jismai hum ye btate h ky kya kya hoga 
    print("------Welcome to the Calculator Program!------")
    def __init__(self,num1,num2): # __init__aik Constructor hota h jab bhi class bny gi tw constructor call hoga .
        #Agr hum constructor nhi lagaty tw python  by Default aik constructor bna deta h ..
        self.num1 = num1
        self.num2=num2
    def add_num(self):
        print(f"Adddition of {self.num1} and {self.num2} is : {self.num1+self.num2}") 
    def sub_num(self):
        print(f"Subtraction of {self.num1} and {self.num2} is : {self.num1-self.num2}")
    def multiply_num(self):
        print(f"Multiplication of {self.num1} and {self.num2} is : {self.num1*self.num2}")
    def divide_num(self):
        print(f"Division of {self.num1} and {self.num2} is : {self.num1/self.num2}")
# Creating an object of the class
#object aik class ka instance hota h ky kaam kya kya hoga
cal= Calculator(10,20)
cal.add_num()
cal.sub_num()
cal.multiply_num()
cal.divide_num()