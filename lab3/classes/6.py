import math

class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds! Withdrawal denied.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")


account = Account("Alice", 200)
account.deposit(100)
account.withdraw(50)
account.withdraw(300)   


is_prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(math.sqrt(n)) + 1))

numbers = [2, 3, 4, 5, 10, 13, 17, 20, 23, 29, 30]
prime_numbers = list(filter(is_prime, numbers))
print("Prime numbers:", prime_numbers)