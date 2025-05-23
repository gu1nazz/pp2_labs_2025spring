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
