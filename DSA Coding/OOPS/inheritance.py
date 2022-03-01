class Person:
    def learn(self):
        print("I am learning")
    def walk(self):
        print("I am walking")
    def eat(self):
        print("I am eating")
class Programmer(Person):
    def code(self):
        print("I am coding")
class Dancer(Person):
    def dance(self):
        print("I am dancing")
class Singer(Person):
    def sing(self):
        print("I am singing")
    def guitar(self):
        print("I am playing guitar")
s = Singer()
s.sing()
s.guitar()
s.learn()
d = Dancer()
d.dance()
d.walk()
p = Programmer()
p.code()
p.eat()