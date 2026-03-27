class BankAccount:
    def __init__(self, status='close', balance=0):
        self.status = status
        self.balance = balance

    def get_balance(self):
        if self.status == 'close':
            raise ValueError('account not open')
        else:
            return self.balance

    def open(self):
        if self.status == 'open':
            raise ValueError('account already open')
        self.status = 'open'


    def deposit(self, amount):
        if self.status == 'close':
            raise ValueError('account not open')
        elif amount <=0:
            raise ValueError('amount must be greater than 0')
        else:
            self.balance += amount
        

    def withdraw(self, amount):
        if self.status == 'close':
            raise ValueError('account not open')
        elif amount < 0:
            raise ValueError('amount must be greater than 0')
        elif amount > self.balance:
            raise ValueError('amount must be less than balance')
        else:
            self.balance -= amount

    def close(self):
        if self.status == "close":
            raise ValueError('account not open')
        self.status = "close"
        self.balance = 0

