# Banking System
# Menu: Deposit, Withdraw, Check Balance.
# Use functions for each operation.
# Keep updating balance after every transaction.


def deposit(balance, amount):
    return balance + amount
def withdraw(balance, amount):
    return balance - amount
def check_balance(balance):
    return balance
print("Menue")
print("1. Deposit")
print("2. Withdraw")
print("3. Check Balance")
choice = input("Enter your choice(1, 2, 3) : ")
balance = 50000
if choice == "1":
    amount = float(input("Enter an amount for deposit : "))
    print(f"Your current balance is {deposit(balance, amount)}")
elif choice == "2":
    amount = float(input("Enter an amount for withdraw : "))
    print(f"Your current balance is {withdraw(balance, amount)}")
elif choice == "3":
    print(f"Your balance is {check_balance(balance)}")
else:
    print("Invalid Choice")
print("Thank you for using our Banking System!")