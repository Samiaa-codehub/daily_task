## task-3 ##
class BankAccount:
    print("----Account Info----")
    def __init__(self, acc_holder,initial_balance):
        self.acc_holder = acc_holder
        self.__initial_balance  = initial_balance


    def deposit_amount(self,amount):
        if amount > 0 :
            self.__initial_balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive")

    def withdraw_amount(self,amount):
        if amount > 0 and amount <= self.__initial_balance:
            self.__initial_balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Withdrawal amount must be positive and less than or equal to the balance")

            
    def get_balance(self):
        return self.__initial_balance
    
    def set_balnce(self,amount):
        if amount > 0:
            self.__initial_balance = amount
            print(f"Balance set to: {amount}")
        else:
            print("Balance must be positive")

    def display_info(self):
        print(f"Account Holder: {self.acc_holder}")
    
    def balance_info(self):
        print(f"Balance: {self.__initial_balance}")

bank = BankAccount("Samia Ali", 0)
bank.display_info()
bank.deposit_amount(1000)
bank.withdraw_amount(500)
bank.get_balance()
bank.balance_info()
print(f"----------------")

bank1 = BankAccount("Ali Khan", 0)
bank1.display_info()
bank1.deposit_amount(2000)
bank1.withdraw_amount(1000)
bank1.get_balance()
bank1.balance_info()
print(f"----------------")

bank2 = BankAccount("Sara Khan", 0)
bank2.display_info()
bank2.deposit_amount(3000)
bank2.withdraw_amount(1500)
bank2.get_balance()
bank2.balance_info()
print(f"----------------")