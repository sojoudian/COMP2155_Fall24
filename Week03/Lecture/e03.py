class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance # Private attribute

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            return "Insufficient funds"
        self.__balance -= amount
        return self.__balance

    def get_balance(self):
        return self.__balance

account1 = BankAccount("Fendi")
account1.deposit(100)
print(account1.get_balance()) # Output: 100
print(account1.withdraw(50)) # Output: 50