class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self._balance=balance #protected variable
    def deposit(self,amount):
        self._balance+=amount
        print("Deposit successful. Current balance:",self._balance)
    def withdraw(self,amount):
        if amount<=self._balance:
            self._balance-=amount
            print("Withdrawal successful. Current balance:",self._balance)
        else:
            print("Insufficient balance.")

    def show_balance(self):
        print(,self._balance)

pin=1234
name=input("enter name")
balance=int(input("enter opening balance"))
pin=int(input("enter pin"))

s=BankAccount(name,balance)

while True:
    print("/n1.deposit 2.withdraw 3.check balnce 4.exit")
    choice=int(input("enter choice"))
    if choice==1:
        amt=int(input("enter choice"))
        s.withdraw(withdraw)
    elif choice ==3:
        s.show_balance()
    elif choice ==4:
        break



