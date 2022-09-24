class BankAccount:
    def __init__(self, balance = 0, int_rate=0.2):
        self.int_rate = int_rate
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        

    def withdraw(self, amount):
        self.balance -= amount
        

    def display_account_info(self):
        print(self.balance, self.int_rate)
        

    def yield_interest(self):
        self.balance = self.balance + (self.balance * self.int_rate) 



class User:		
    def __init__(self, name):
        self.name = name
        self.account = BankAccount(int_rate=0.02, balance=0)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        # print(self.name)
        print( self.name,self.account.balance)
        return self




mjd = User("mjd")
mjd.make_deposit(100).make_withdrawal(50)
mjd.display_user_balance()	


