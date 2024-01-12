class Bank:
    accno:int
    balance:int
    ac_type=str
    p_name=str

    def create_account(self,accno,balance,ac_type,name):
        self.accno=accno
        self.balance=balance
        self.ac_type=ac_type
        self.p_name=name
    def deposit(self,amount):
        self.balance+=amount
        print(f"your sbk account{self.accno} has been credited with amount {amount}availble balance is{self.balance}")

    def withdraw(self,amount):
            if self.balance>=amount:
                self.balance-=amount
                print(f"your sbk account{self.accno} has been credited with amount {amount}availble balance is{self.balance}")
            else:
                print("transaction failed insufficient balance")
obj1=Bank()
obj1.create_account(100,2000,"savings","hari")

obj1.withdraw(1000)



