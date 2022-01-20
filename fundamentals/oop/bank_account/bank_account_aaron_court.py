class BankAccount:
    bank_name = "First National Bank of Aarontopia"
    all_accts = []
    acct_num = 1001

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        self.int_percent = int_rate * 100
        self.acct_num = BankAccount.acct_num
        BankAccount.all_accts.append(self)
        BankAccount.acct_num += 1
        # print(BankAccount.all_accts)

    @classmethod
    def all_accounts(cls):
        for accts in cls.all_accts:
            accts.display_acct_info()

    def deposit(self, amt):
        self.balance += amt
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
            self.balance = self.balance + (self.balance * self.int_rate)
            print(self.balance)
            
        return self

acct1 = BankAccount(.05,0)
acct2 = BankAccount(.10, 100)

acct1.deposit(25).deposit(30).deposit(200).withdraw(180).display_acct_info().yield_int()
acct2.deposit(150).deposit(75).withdraw(40).withdraw(25).withdraw(200).withdraw(90).display_acct_info().yield_int()
print('')
BankAccount.all_accounts()