# Bank Account Program

balance = 0

def display_balance():
    print("Current Balance:", balance)

def deposit(amount):
    global balance
    balance += amount
    print("Amount Deposited Successfully")

def withdraw(amount):
    global balance
    if amount > balance:
        print("Insufficient Balance")
    else:
        balance -= amount
        print("Amount Withdrawn Successfully")

while True:
    print("\n---- BANK MENU ----")
    print("1. Display Current Balance")
    print("2. Deposit Amount")
    print("3. Withdraw Amount")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 4:
        print("Thank You!")
        break

    if choice == 1:
        display_balance()

    elif choice == 2:
        amt = float(input("Enter amount to deposit: "))
        deposit(amt)

    elif choice == 3:
        amt = float(input("Enter amount to withdraw: "))
        withdraw(amt)

    else:
        print("Invalid Choice")