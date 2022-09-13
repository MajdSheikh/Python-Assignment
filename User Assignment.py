
class User:		
    def __init__(self, name, account_balance):
        self.name = name
        self.account_balance = account_balance

    def make_deposit(self, amount):
        self.account_balance += amount
    
    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(self.name, self.account_balance)

    def transfer_money(self, user, amount):
        self.account_balance = self.account_balance - amount
        user.account_balance = user.account_balance + amount 


zen = User("zen", 100)
zen.make_deposit(100)
zen.make_deposit(100)
zen.make_deposit(100)
zen.make_withdrawal(20)
zen.display_user_balance()


moh = User("moh", 200)
moh.make_deposit(100)
moh.make_deposit(100)
moh.make_withdrawal(70)
moh.make_withdrawal(90)
moh.display_user_balance()


sal = User("sal", 300)
sal.make_deposit(100)
sal.make_withdrawal(50)
sal.make_withdrawal(50)
sal.make_withdrawal(50)
sal.display_user_balance()



zen.transfer_money(sal, 200)
zen.display_user_balance()
sal.display_user_balance()


