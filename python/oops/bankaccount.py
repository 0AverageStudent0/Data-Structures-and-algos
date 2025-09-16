#Design a BankAccount class with deposit, withdraw, and balance inquiry methods. Use encapsulation to protect balance.
class BankAccount:
    def __init__(self,c_name,acc_number,balance):
        self.c_name = c_name
        self.acc_number = acc_number
        self.__balance = balance
        self.transaction = []

    def view_transaction(self):
        if not self.transaction:
            print("no transactions yet") 
        else:
            for entry in self.transaction:
                if entry < 0:
                    print(f"debited : {entry}")
                else:
                    print(f"credited : {entry}")      

    def check_bal(self):
        print(f"Current Balance: ₹{self.__balance}")
    
    def apply_intrest(self,intrest):
        intrest = abs(intrest)
        intrest = intrest * 0.01
        intrest_amount = self.__balance*intrest
        print(f"Intrest amount is : ₹{intrest_amount}")
        self.__balance += intrest_amount
          
    def withdraw(self,amount):
        if amount <= 0 :
            print("Please enter an valid amount")
        elif amount > self.__balance:
            print("Insufficient Funds")
        elif amount <= self.__balance:
            if amount <= 5000:
                self.__balance -= amount
                print(f"Total Balance ₹{self.__balance}")
                self.transaction.append(-1*amount)
            else:
                print("You can only withdraw upto 5000")

    def deposit(self,amount):
        self.__balance += amount
        print(f"Total Balance ₹{self.__balance}")
        self.transaction.append(amount)
        



c1 = BankAccount("rasheed",1234567,10000)
c1.check_bal()
c1.apply_intrest(5)
# c1.withdraw(100)
# c1.deposit(1)
# c1.deposit(1000)
# c1.view_transaction()