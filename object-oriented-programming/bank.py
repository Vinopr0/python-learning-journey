
class Bank():
    
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else: 
            self.balance -= amount

    def __str__(self):
        return f"Funds in {self.owner}'s account: {self.balance}$"


bank1 = Bank("Jose", 3000)

print(bank1)

bank1.withdraw(300)

print(bank1)

bank1.deposit(200)

print(bank1)

bank1.withdraw(3000)