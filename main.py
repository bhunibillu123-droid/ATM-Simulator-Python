# ATM Simulator in Python

pin = 1234
balance = 10000
transactions = []

entered_pin = int(input("Enter Your 4-Digit ATM PIN: "))

if entered_pin == pin:

    print("\n**** WELCOME TO ATM ****")

    while True:

        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Mini Statement")
        print("5. Exit")

        choice = int(input("Enter Your Choice: "))

        if choice == 1:
            print("\nCurrent Balance: ₹", balance)

        elif choice == 2:
            amount = float(input("Enter Deposit Amount: ₹"))

            if amount > 0:
                balance += amount
                transactions.append(f"Deposited ₹{amount}")
                print("Amount Deposited Successfully!")
                print("Current Balance: ₹", balance)
            else:
                print("Invalid Amount!")

        elif choice == 3:
            amount = float(input("Enter Withdrawal Amount: ₹"))

            if amount <= 0:
                print("Invalid Amount!")

            elif amount > balance:
                print("Insufficient Balance!")

            else:
                balance -= amount
                transactions.append(f"Withdrawn ₹{amount}")
                print("Please Collect Your Cash.")
                print("Remaining Balance: ₹", balance)

        elif choice == 4:

            print("\n===== MINI STATEMENT =====")

            if len(transactions) == 0:
                print("No Transactions Yet.")

            else:
                for transaction in transactions:
                    print(transaction)

            print("Current Balance: ₹", balance)

        elif choice == 5:
            print("\nThank You For Using Our ATM.")
            print("Visit Again!")
            break

        else:
            print("Invalid Choice! Please Try Again.")

else:
    print("Incorrect PIN! Access Denied.")