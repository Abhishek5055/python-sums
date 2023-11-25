class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

# Creating a bank account
account = BankAccount(1000)

# Accessing balance through a method
print(account.get_balance())  # Output: 1000

# Depositing and withdrawing using methods
account.deposit(500)
account.withdraw(200)
print(account.get_balance())  # Output: 1300
