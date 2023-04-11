
class BankAccount:
    def __init__(self, balance):
        # Private attribute 
        self.__balance = balance
        # Protected attribute 
        self._transaction_history = []

    # Private function 
    def __update_balance(self, amount):
        self.__balance += amount
        self._transaction_history.append(amount)

    # Public function 
    def deposit(self, amount):
        self.__update_balance(amount)
    
    # Public function 
    def withdraw(self, amount):
        self.__update_balance(-amount)

    # Public function - can be called from outside the class
    def get_balance(self):
        return self.__balance

# Create a bank account with a starting balance of $1000
account = BankAccount(1000)

# Deposit $500 into the account
account.deposit(500)

# Withdraw $200 from the account
account.withdraw(200)

# Get the current balance of the account
balance = account.get_balance()

# Print the balance and transaction history
print("Current balance:", balance)
print("Transaction history:", account._transaction_history)
