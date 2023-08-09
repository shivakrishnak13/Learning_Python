class BankAccount :
    def __init__(self, account_holder, balance) :
        self.account_holder = account_holder
        self.balance = balance
       
    def deposit(self, amount) :
         self.balance += amount
         return self.balance
    
    def withdraw(self, amount) :
        self.balance -= amount
        return self.balance

    def get_balance(self) :
        return self.balance
    

b1 = BankAccount('shiva',0)
b1.deposit(100)
b1.withdraw(50)
print(b1)


#file handling

file = open("./sample.txt","r")

fileread = file.read()
print(fileread)