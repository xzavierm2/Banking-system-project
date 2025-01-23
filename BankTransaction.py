# Xzavier Morgan

# Menu for the customer to see
def menu():
    print("\n***************************")
    print("\nMenu for the following options: ")
    print("1. Deposit\n2. Withdraw\n3. Transfer\n4. Check Balance\n5. Exit")
    print("\n***************************")

# Deposit into balance.
def deposit(balance):
    while True:
        try:
            amount = float(input("Enter an amount to deposit: "))
            if amount < 0:
                print("Amount must be positive.")
            else:
                balance += amount
                print(f"\nYou have deposited ${amount:.2f}. This is your new balance ${balance:.2f}.")
                return balance
        except ValueError:
            print("Invalid Input. ")

# Withdraw from balance.
def withdraw(balance):
    while True:
        try:
            amount = float(input("Enter the amount you would like to withdraw: "))
            if amount < 0:
                print("Amount must be positive. ")
            elif amount > balance:
                print("Insufficient funds avaliable.")
            else:
                balance -= amount
                print(f"\nYou have withdrawn ${amount:.2f}. Your new balance is ${balance:.2f}.")
                return balance
        except ValueError:
            print("Invalid Input. ")
    
# Transfer to another.    
def transfer(balance):
    while True:
        try:
            amount = float(input("Enter an amount to Transfer: $"))
            if amount > balance:
                print("Insuffiecient funds. Not able to make Transfer.")
            elif amount > balance:
                print("Insufficient funds avaliable.")
            else: 
                recipient = input("Enter recipient name: ")
                balance -= amount
                print(f"\nYou have successfuly transfered ${amount:.2f} to {recipient}'s account. This is your new account balance ${balance:.2f}.")
                return balance
        except ValueError:
            print("Transfer cannot be made.")

# Check balance
def check_balance(balance):
     print(f"\nThe current balance is ${balance:.2f}.")

# Main function
def main():
    account_number = "12345678"
    pin_number = "1234"

    print("Welcome to the Bank")
    # If user enters wrong pin
    attempts = 3

    while attempts > 0:
        entered_account = input("Please enter account number: ")
        entered_pin = input("Please enter your pin number: ")

# Matching account number and Pin to login
        if entered_account == account_number and entered_pin == pin_number:
            print("\nLogin is Successful.")
            balance = 0.0

            while True:
                menu()

                try:
                    option = input("Select from choices (1-5): ")
                    if option == "1":
                       balance = deposit(balance)
                    elif option == "2":
                        balance = withdraw(balance)
                    elif option == "3":
                        balance = transfer(balance)
                    elif option == "4":
                        check_balance(balance)
                    elif option == "5":
                        print(" Thank you for using the Bank")
                        break
                    else:
                        print("Please choose options (1-5):\n")
                except ValueError:
                    print("Invalid Input")
            break      
        else:
            attempts -= 1
            if attempts > 0:
                    print(f" Incorrect account number or pin. You have {attempts} attempts left. ")
            else:
                print("Incorrect account number or pin has been entered too many times. Access Denied")

# Calling Main Function
if __name__ == "__main__":
    main()    
        



    