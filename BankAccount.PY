
class BankAccount:
    def __init__(self, balance = 0, int_rate=0.1):
        self.int_rate = int_rate
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print(self.balance, self.int_rate)
        return self

    def yield_interest(self):
        self.balance = self.balance + (self.balance * self.int_rate) 
        return self

mjd = BankAccount(100)
mjd.deposit(100).deposit(50).deposit(60).withdraw(100).yield_interest().display_account_info()


rhf = BankAccount(200)
rhf.deposit(100).deposit(100).withdraw(40).withdraw(40).withdraw(40).withdraw(40).yield_interest().display_account_info()


