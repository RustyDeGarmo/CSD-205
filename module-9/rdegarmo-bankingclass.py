'''
Rusty DeGarmo
Professor Payne
Intro to Programming with Python
1 May 2021
'''

#This program is to display class and inheritance functionality within
#a banking application.

#define the parent class bankAccount with paramaters and functions that
#all bank accounts will have
class bankAccount:
    #define the mandatory init function and set the applicable parameters
    def __init__(self, accountNumber, balance):
        self.accountNumber = accountNumber
        self.balance = balance

    #define a withdrawl function
    def withdrawl(self):
        prompt = "\nHow much do you want to withdraw? "
        withdrawAmount = input(prompt)
        if withdrawAmount == "4":
            condition = False
            
        self.balance -= float(withdrawAmount)

    #define a deposit function
    def deposit(self):
        prompt = "\nHow much do you want to deposit? "
        depositAmount = input(prompt)
        if depositAmount == "4":
            condition = False

        self.balance += float(depositAmount)

    #define a function to show the user what their balance is
    def getBalance(self):
        print(f"\nYour current balance is ${self.balance}")
        return self.balance


#define a savings account class that inherits the parameters and functions
#from the bank account class
class savingsAccount(bankAccount):
    #define the init function to add the interest rate parameter to this 
    #account type class
    def __init__(self, accountNumber, balance, interestRate, accountType = "Savings"):
        super().__init__(accountNumber, balance)
        self.accountType = accountType
        self.interestRate = interestRate / 100
        

    #define a function that increments the current balance by the accrued
    #interest that can be called once per year. Assuming that interest on this 
    #account only compounds once per year.
    def addInterest(self):
        self.balance += self.balance * self.interestRate
        print(f"Your balance is now {self.balance}")

#define a checking account class that inherits the parameters and functions 
#from the bank account class
class checkingAccount(bankAccount):
    #define the init function to include applicible fees and balance requirements
    #for this account type
    def __init__(self, accountNumber, balance, fees = 5, minBalance = 50, \
        accountType = "Checking"):
        super().__init__(accountNumber, balance)
        self.accountType = accountType
        self.fees = fees
        self.minBalance = minBalance

    #define a function that deducts the fees from the current balance
    def deductFees(self):
        return self.balance - self.fees

    #define a function that checks to see if the current balance is below the
    #minimum balance for this account type and calls the deductFees function
    #if so.
    def checkMinBalance(self):
        if self.balance < self.minBalance:
            print(f"Your current balance of ${self.balance} is below the \
minimum balance of ${self.minBalance}. A fee of ${self.fees} will be deducted \
from your account at the end of the month.")
            print(f"Your remaining balance will be ${self.deductFees()}")

        else: print(f"Your balance is above the minimum balance of \
{self.minBalance}. Congratulations, you don't owe any fees!")

#define a function to print basic account information
def printAccountInfo(bankAcc):
        print(f"Bank Account Number: {bankAcc.accountNumber}")
        print(f"Account Type: {bankAcc.accountType}")
        print(f"Account Balance: ${bankAcc.balance}")

#create and print information for two checking account objects and 
#one savings account object for class testing and assignment requirements
checking1 = checkingAccount("12345", 200, 5, 50)
print()
printAccountInfo(checking1)
checking1.checkMinBalance()

checking2 = checkingAccount("23456", 25, 5, 50)
print()
printAccountInfo(checking2)
checking2.checkMinBalance()

savings1 = savingsAccount("34567", 200, 2)
print()
printAccountInfo(savings1)
savings1.addInterest()

#create a list that contains our bank accounts and a list that contains our
#account numbers so we can check later to see if the user has selected a
#valid account
accountsList = [checking1, checking2, savings1]
accountNumbers = []
for account in accountsList:
    accountNumbers.append(account.accountNumber)


#set a condition variable to True so our user will be able to choose when to 
#end the program
condition = True
while condition:
    #Greet the client and ask them to select an account. I'm assuming they have
    #already logged in
    print("\nHello, enter 4 to quit at any time. Your accounts are: ")
    for account in accountsList:
        print(f"{account.accountType}: {account.accountNumber}")

    #prompt the user to select an account
    accountPrompt = "Select an account number: "
    accountSelection = input(accountPrompt)
    if accountSelection == "4":
        condition = False
        continue

    #create some space
    print()
    print()

    #check to see if the selected account exists and then store the selected
    #account in a local veriable
    #I know there must be a more dynamic and intuitive way to do this but I haven't
    #figured it out and I'm running out of time
    if accountSelection in accountNumbers:
        for account in accountsList:
            if accountSelection == "12345":
                account = checking1
            elif accountSelection == "23456":
                account = checking2
            else:
                account = savings1
        #Provide a list of available options.
        print("The available banking functions for this account are:\
\n1: Deposit\
\n2: Withdraw\
\n3: Balance\
\n4: Quit")

        #create a prompt variable to keep the input call clean
        optionPrompt = "Select an numerical option (1, 2, 3, or 4): "
        #get the user's selection
        userOption = input(optionPrompt)

        #test the user input for the correct type
        try:
            int(userOption)
        except:
            print("\nYou didn't enter a number. Try again.")
            continue

        #Process the user selection and call the applicable function
        if userOption == "1":
            account.deposit()
        elif userOption == "2":
            account.withdrawl()
        elif userOption == "3":
            account.getBalance()
        elif userOption == "4":
            condition = False
            continue
        else:
            print("That was not one of the available options. Try again.")
            continue
    else:
        print("That is not a valid account number. Try again.")
        continue





'''
py rdegarmo-bankingclass.py
'''

