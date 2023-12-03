class BankAccount:
    def __init__(self,bank_name,owner_name,account,number,current_balance):
        self.bank_name = bank_name
        self.owner_name = owner_name
        self.account = account
        self.number = number
        self.current_balance = current_balance
    def deposit(self,amount):
        if amount<self.current_balance:
            if amount <0:
                self.current_balance -= amount
            elif amount >0:
                self.current_balance += amount
    def withdraw(self,amount):
        if amount<self.current_balance:
            if amount <0:
                self.current_balance += amount
            elif amount >=0:
                self.current_balance -= amount
    def __str__(self):
        return f"{self.bank_name},{self.owner_name},{self.account},{self.number},{self.current_balance}"
    def print(self):
        print(self)
BankAccount1 = BankAccount("K_Bank","Arhway",4353_322,2948,324233)
BankAccount1.deposit(0)
BankAccount1.withdraw(-100)
BankAccount1.print()

