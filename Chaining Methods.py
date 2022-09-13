class User:		
    def __init__(self, name, account_balance):
        self.name = name
        self.account_balance = account_balance
        

    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(self.name, self.account_balance)
        return self

    def transfer_money(self, user, amount):
        self.account_balance = self.account_balance - amount
        user.account_balance = user.account_balance + amount 
        return self

zen = User("zen", 100)
moh = User("moh", 200)
sal = User("sal", 300)

zen.make_deposit(100).make_withdrawal(50).display_user_balance()

moh.make_deposit(100).make_withdrawal(70).display_user_balance()

sal.make_deposit(100).make_withdrawal(50).display_user_balance()