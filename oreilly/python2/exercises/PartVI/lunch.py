class Lunch:
    def __init__(self):            # make/embed Customer and Employee
        self.cust = Customer()
        self.empl = Employee()
    def order(self, foodName):     # start a Customer order simulation
        self.cust.placeOrder(foodName, self.empl)
    def result(self):              # ask the Customer about its Food
        self.cust.printFood()

class Customer:
    def __init__(self):                       # initialize my food to None
        self.food = None
    def placeOrder(self, foodName, employee):  # place order with Employee
        self.food = employee.takeOrder(foodName)
    def printFood(self):                       # print the name of my food
        print self.food.name

class Employee:
    def takeOrder(self, foodName):    # return a Food, with requested name
        return Food(foodName)

class Food:
    def __init__(self, name):          # store food name
        self.name = name

if __name__ == '__main__':
    x = Lunch()                       # self-test code
    x.order('burritos')               # if run, not imported
    x.result()
    x.order('pizza')
    x.result()
