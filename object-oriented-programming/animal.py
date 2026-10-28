class Dog():
    # class object atrribute (for any class)
    type_of_animal = 'mammal'


    def __init__(self, breed, weight, name="Rex"):
        self.name = name
        self.breed = breed
        self.weight = weight
    
    # operations / actions --> methods
    
    def bark(self):
        print("woof!")

dog1 = Dog(breed="Huskie", weight=11.4)

print(dog1.name)

print(dog1.type_of_animal)