class Animal():

    def __init__(self):
        print("Animal created")

    def eat(self):
        print("I am eating")

    def who_am_i(self):
        print("I am an animal")

class Dog(Animal): # derived class!
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

    # you can overwrite a method here if you want to:
    def eat(self):
        print("*woofs and munches*")

mydog = Dog()

mydog.eat()