# For this assignment, we'll add some functionality to the User class:

# make_withdrawal(self, amount) - have this method decrease the user's balance by the amount specified

# display_user_balance(self) - have this method print the user's name and account balance to the terminal
# eg. "User: Guido van Rossum, Balance: $150

# BONUS: transfer_money(self, other_user, amount) - have this method decrease the user's balance by the amount and add that amount to other other_user's balance

class User:
    def __init__(self, first_name, last_name):
        self.name = first_name + ' ' + last_name
        self.balance = 0

    def make_deposit(self, amount):
        self.balance += amount
        return self

    def make_withdrawl(self, amount):
        self.balance -= amount
        return self

    def display_balance(self):
        print(f'Hello {self.name}. Your balance is: ${self.balance}.')
        return self

    def make_transfer(self, other_user, amount):
        self.balance -= amount
        print(f'Hello {self.name}. Your transfer is complete and your new balance is ${self.balance}')
        other_user.balance += amount
        print(f'Hello {other_user.name}. A transfer was made into your account. Your new balance is ${other_user.balance}')
        return self

david_beckham = User('David', 'Beckam')
daniel_radcliff = User('Daniel', 'Radcliff')
halle_berry = User('Halle', 'Berry')

david_beckham.make_deposit(25).make_deposit(75).make_deposit(42).make_withdrawl(100).display_balance()

halle_berry.make_deposit(400).make_withdrawl(125).make_withdrawl(260).make_withdrawl(55).display_balance()

daniel_radcliff.make_deposit(200).make_deposit(60).make_withdrawl(33).make_withdrawl(120).display_balance().make_transfer(halle_berry, 50)