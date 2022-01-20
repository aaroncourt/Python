class User:
    def __init__(self, first_name, last_name, int_rate, amt):
        self.name = first_name + ' ' + last_name
        self.checking = BankAccount(int_rate, amt)

    def make_deposit(self, amount):
        self.checking.balance += amount
        return self

    def make_withdrawl(self, amount):
        self.checking.balance -= amount
        return self

    def display_balance(self):
        print(f'Hello {self.name}. Your balance is: ${self.checking.balance}.')
        return self

    def make_transfer(self, other_user, amount):
        self.checking -= amount
        print(f'Hello {self.name}. Your transfer is complete and your new balance is ${self.checking.balance}')
        other_user.checking += amount
        print(f'Hello {other_user.name}. A transfer was made into your account. Your new balance is ${other_user.checking}')
        return self

class BankAccount():
    bank_name = "First National Bank of Aarontopia"
    all_accts = []
    acct_num = 1001

    def __init__(self, int_rate, amt):
        self.int_rate = int_rate
        self.int_percent = int_rate * 100
        self.balance = amt
        self.acct_num = BankAccount.acct_num
        BankAccount.all_accts.append(self)
        BankAccount.acct_num += 1
        print(self.acct_num)

    @classmethod
    def all_accounts(cls):
        for accts in cls.all_accts:
            accts.display_acct_info()

    def deposit(self, amt):
        self.account += amt
        return self

    def withdraw(self, amt):
        if (self.balance - amt) <= 0:
            print('Insufficient funds: Charging a $5 fee.')
            self.balance -= 5
        else:
            self.balance -= amt
        return self

    def display_acct_info(self):
        print(f'Account number: {self.acct_num}. Your account balance is {self.balance}. Your account yield is {self.int_percent}%.')
        return self

    def yield_int(self):
        if self.balance <= 0:
            print('The balance to too low to yield interest.')
        else:
            self.balance += (self.balance * self.int_rate)
            print(self.balance)
            
        return self

tom_holland = User('Tom', 'Holland', .01, 100)

tom_holland.display_balance().make_deposit(25).display_balance()

