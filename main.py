
# ATM SIMULATOR PROJECT #
from datetime import datetime
def print_receipt(transaction_type, amount, balance):

    print("\n====================================")
    print("         SBI ATM RECEIPT")
    print("====================================")
    print("Date :", datetime.now().strftime("%d-%m-%Y"))
    print("Time :", datetime.now().strftime("%I:%M:%S %p"))
    print("------------------------------------")
    print("Transaction :", transaction_type)
    print("Amount      : ₹", amount)
    print("Balance     : ₹", balance)
    print("------------------------------------")
    print("Thank You For Banking With SBI")
    print("Visit Again!")
    print("====================================")
pin = 1234
balance = 10000
transactions = []

entered_pin = int(input("Enter Your 4-Digit ATM PIN: "))
if entered_pin == pin:

 print("\n=================================================")
print("        STATE BANK OF INDIA")
print("           ATM SIMULATOR")
print("=================================================")
print(" Welcome to SBI ATM")
print(" Please insert your card (Simulation)")
print("=================================================")

now = datetime.now()
print("Date :", now.strftime("%d-%m-%Y"))
print("Time :", now.strftime("%I:%M:%S %p"))
print("=================================================")

while True:

        print("\n======================================")
        print("            ATM MAIN MENU")
        print("======================================")
        print("[1] 💰 Check Balance")
        print("[2] 💵 Deposit Money")
        print("[3] 💸 Withdraw Money")
        print("[4] 📄 Mini Statement")
        print("[5] 🔐 Change ATM PIN")
        print("[6] 💵 Fast Cash")
        print("[7] 🚪 Exit")
        print("======================================")

        choice = int(input("Enter Your Choice: "))

        # Check Balance
        if choice == 1:
            print("\nCurrent Balance: ₹", balance)

        # Deposit Money
        elif choice == 2:
            amount = int(input("Enter Amount to Deposit: ₹"))

            if amount > 0:
                balance += amount
                transactions.append(
    f"{datetime.now().strftime('%d-%m-%Y %I:%M:%S %p')} - Deposited ₹{amount}"
)
                print("₹", amount, "Deposited Successfully.")
            else:
                print("Invalid Amount!")

        # Withdraw Money
        elif choice == 3:
            amount = int(input("Enter Amount to Withdraw: ₹"))

            if amount <= balance:
                balance -= amount
                transactions.append(
    f"{datetime.now().strftime('%d-%m-%Y %I:%M:%S %p')} - Withdrawn ₹{amount}"
)
                print("Please Collect Your Cash.")
                print("Remaining Balance: ₹", balance)
            else:
                print("Insufficient Balance!")

        # Mini Statement
        elif choice == 4:

            print("\n===== MINI STATEMENT =====")

            if len(transactions) == 0:
                print("No Transactions Yet.")
            else:
                for transaction in transactions:
                    print(transaction)

            print("Current Balance: ₹", balance)

        # Change PIN
        elif choice == 5:

            old_pin = int(input("Enter Current PIN: "))

            if old_pin == pin:
                new_pin = int(input("Enter New 4-Digit PIN: "))
                pin = new_pin
                print("PIN Changed Successfully.")
            else:
                print("Incorrect Current PIN!")

        #Fast Cash
        elif choice == 6:
            print("\n===== FAST CASH =====")
            print("1. ₹500")
            print("2. ₹1000")
            print("3. ₹2000")
            print("4. ₹5000")
            print("5. Back")

            fast_choice = int(input("Select Amount: "))
            if fast_choice == 1:
              amount = 500
        elif fast_choice == 2:
            amount = 1000
        elif fast_choice == 3:
            amount = 2000
        elif fast_choice == 4:
            amount = 5000
        elif fast_choice == 5:
          continue
        else:
          print("Invalid Choice!")
        
        continue

        if amount <= balance:
            balance -= amount
            transactions.append(
                f"{datetime.now().strftime('%d-%m-%Y %I:%M:%S %p')} - Fast Cash ₹{amount}"
            )
            print("Please Collect Your Cash.")
            print("Withdrawn: ₹", amount)
            print("Remaining Balance: ₹", balance)
        else:
            print("Insufficient Balance!")

        choice == 7
        print("\nThank You For Using Our ATM.")
        print("Visit Again!")
        break

else:
            print("Invalid Choice! Please Try Again.")