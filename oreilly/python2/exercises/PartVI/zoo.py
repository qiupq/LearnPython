class Animal:
    def reply(self):   self.speak()        # back to subclass
    def speak(self):   print 'spam'        # custom message

class Mammal(Animal):
    def speak(self):   print 'huh?'

class Cat(Mammal):
    def speak(self):   print 'meow'

class Dog(Mammal):
    def speak(self):   print 'bark'

class Primate(Mammal):
    def speak(self):   print 'Hello world!'

class Hacker(Primate): pass                # inherit from Primate

if __name__ == '__main__':
    spot = Cat()
    spot.reply()        # Animal.reply, calls Cat.speak
    data = Hacker()     # Animal.reply, calls Primate.speak
    data.reply()
