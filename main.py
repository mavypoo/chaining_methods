class User: 
    def __init__(self, name):
        self.name = name
        self.amount = 0 

    def make_deposit(self,amount):
        self.amount += amount
        return self 

    def make_withdrawal(self,amount):
        self.amount -= amount 
        return self
    
    def display_user_balance(self):
        print(f'User: {self.name}, Balance: {self.amount}')
        return self 


mav = User('Maverick')
rob = User('Robby')
derek = User('Derek')

mav.make_deposit(500).make_deposit(100).make_deposit(200).make_withdrawal(50).display_user_balance()
rob.make_deposit(200).make_deposit(200).make_withdrawal(50).make_withdrawal(50).display_user_balance()
derek.make_deposit(400).make_withdrawal(100).make_withdrawal(100).make_withdrawal(500).display_user_balance()
