class BankAccount:

    def __init__(self, int_rate = 0.01, balance = 0): 
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        return self

    def display_account_info(self):
        print(f'Interest Rate : {self.int_rate}\nBalance : {self.balance}')
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * 0.01
        return self


account1 = BankAccount()
account2 = BankAccount()

account1.deposit(amount=100).deposit(amount=100).deposit(amount=100).withdraw(amount=100).yield_interest().display_account_info()

account2.deposit(amount=100).deposit(amount=500).withdraw(amount=50).withdraw(amount=50).withdraw(amount=50).withdraw(amount=50).yield_interest().display_account_info()