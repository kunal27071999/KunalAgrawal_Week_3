"""
21. Create class as AccountHolder with attributes as name, age, bank account balance and withrawal request amount.
Create the user defined exception to handle
		- Throw InvalidNameError if account holder name contains number 
		- Throw TooYoung or TooOld exception if account holder age is below 18 or more that 58
		- Throw InsufficientFundsException if account balanceis less that withrawal request amount

"""

class AccountHolder:
    def __init__(self,name,age,balance,withdrawl):
        self.name=name
        self.age=age
        self.balance=balance
        self.withdrawl=withdrawl
    def disp(self):
        try:
            print("Account created")
        except(self.name.isdigit()):
            raise ("Name")
            print("Name contains number")
        except(self.age<18 or self.age>58):
            raise ("Age")
            print("Invalid age")
        except(self.balance<self.withdrawl):
            raise ("Balance")
            print("Invalid Amount")

obj1=AccountHolder('KUNAL123',20,100,1)
obj1.disp()