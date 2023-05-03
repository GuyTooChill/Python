class user:

    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

    def make_deposit(self, amount):
        self.account.balance += amount
        return self
    
    def make_withdraw(self, amount):
        if self.account.balance >= amount:
            self.account.balance -= amount
        return self

    def display_account_info(self):
        print(f'Name : {self.name}\nEmail : {self.email}\nInterest Rate : {self.account.int_rate}\nBalance : {self.account.balance}')
        return self



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





user1 = user('Diego', 'diego123456789@gmail.com')
user2 = user('Briona', 'briona123456789@gmail.com')



user1.make_deposit(amount=500)
user1.make_withdraw(amount=200)
user1.display_account_info()