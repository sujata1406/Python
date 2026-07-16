class BankAccount:

    ROI=10.5

    def __init__(self):
        self.Name=input("Enter Account holder Name : " )
        self.Amount=float(input("Enter Amount : "))

    def Display(self):
        print("Name is : ",self.Name)
        print("Amount is : ",self.Amount)

    def Deposit(self):
        Balance=float(input("Enter Deposit amount : "))
        self.Amount=self.Amount+Balance

    def Withdraw(self):
        Withdraw_amount=float(input("Enter withdraw amount : "))
        if Withdraw_amount <= self.Amount:
            self.Amount=self.Amount-Withdraw_amount

        else:
            print("Insufficient amount in account")

    def CalculateInterest(self):
        Interest=(self.Amount*BankAccount.ROI)/100
        print("Intrest is : ",Interest)


Bobj1=BankAccount()

Bobj1.Display()
Bobj1.Deposit()
Bobj1.Display()
Bobj1.Withdraw()
Bobj1.Display()
Bobj1.CalculateInterest()
Bobj1.Display()

    

