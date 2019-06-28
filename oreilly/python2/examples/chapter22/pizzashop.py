from employees import PizzaRobot, Server

class Customer:
    def __init__(self, name):
        self.name = name
    def order(self, server):
        print self.name, "orders from", server
    def pay(self, server):
        print self.name, "pays for item to", server

class Oven:
    def bake(self):
        print "oven bakes"

class PizzaShop:
    def __init__(self):
        self.server = Server('Pat')         # embed other objects
        self.chef   = PizzaRobot('Bob')     # a robot named bob
        self.oven   = Oven()

    def order(self, name):
        customer = Customer(name)           # activate other objects
        customer.order(self.server)         # customer orders from server
        self.chef.work()
        self.oven.bake()
        customer.pay(self.server)

if __name__ == "__main__":
    scene = PizzaShop()                     # make the composite
    scene.order('Homer')                    # simulate Homer's order
    print '...'
    scene.order('Shaggy')                   # simulate Shaggy's order
