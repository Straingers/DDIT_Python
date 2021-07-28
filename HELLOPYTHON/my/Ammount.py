class Account:
    def __init__(self, accountNo, ownerName, balance):
        self.accountNo = accountNo
        self.ownerName = ownerName
        self.balance = balance
    
    def withdraw(self, amount):
        if self.balance < amount:
            print("잔액이 부족합니다")
            return 
        else:
            self.balance = self.balance - amount