class atm(object):
    def __init__(self,exisitingAmount,pin,cashWithdrawn):
        self.exisitingAmount = exisitingAmount
        self.pin = pi
        self.cashWithdrawn = cashWithdrawn
        self.currentBalance = 5000.00

    def intro(self):
        print("Welcome to Sadana's ATM")
        print("Here, you can withdraw cash from your existing account")
        print("And, check your exisiting balance")

    def enterPin(self):
        input("Enter your PIN")

    def checkBalance(self):
        print("Your current balance: INR ", currentBalance)

    def withdrawCash(self):
        cash = input("Enter the amount to be withdrawn: ")
        newCurrentBalance = currentBalance - cash
        print(cash, "INR has been withdrawn from your account")
        print("Thanks for using Sadana's atm :)")

    at = atm(5000,3125,200)
    at.intro()

