class Actor:
    def line(self): print self.name + ':', `self.says()`

class Customer(Actor):
    name = 'customer'
    def says(self): return "that's one ex-bird!"

class Clerk(Actor):
    name = 'clerk'
    def says(self): return "no it isn't..."

class Parrot(Actor):
    name = 'parrot'
    def says(self): return None

class Scene:
    def __init__(self):
        self.clerk    = Clerk()       # embed some instances
        self.customer = Customer()    # Scene is a composite
        self.subject  = Parrot()

    def action(self):
        self.customer.line()          # delegate to embedded
        self.clerk.line()
        self.subject.line()

if __name__ == '__main__':
    Scene().action()     # or import parrot interactively
