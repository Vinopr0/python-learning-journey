
# dunder / magic methods

class Book():

    def __init__(self, name, pages, author):
        self.name = name
        self.pages = pages
        self.author = author

    def __str__(self): # returns something when asked for a string of the object instance
        return f"The book name is {self.name}, made by {self.author}, and has {self.pages} pages."

    def __len__(self): # returns something when asked for the length of the object instance
        return self.pages

    def __del__(self):
        return print(f"{self.name} has been deleted.")

b = Book(name="One Year of Solitude", pages=300, author="Pierre")

print(b) # prints the result of the __str__ special method.

print(len(b))

del b # deletes b from memory

try:
    print(b)
except:
    print("b does not exist anymore.")