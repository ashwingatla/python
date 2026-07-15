# Requirement : Design an ATM system.

# When we run the application it should show Menu Options like below

#         1. Check Balance
#         2. Deposit
#         3. Withdraw
#         4. Exit

# => Take input from user, based on given input perform the action.

balance = 1000
while True:

    print("Menu options offered : \n1.Check Balance \n2.Deposit \n3.Withdraw \n4.Exit")
    try:
        user_input = int(input("Select the type of operation to be performed from the menu:"))
    except ValueError:
        print("Please enter a valid number")
        continue

    match user_input:
        case 1:
            print("user selected : Check Balance")
            print(f"Display balance - {balance}")
        case 2:
            print("user selected : Deposit")
            deposit = int(input("Enter the amount to deposit: "))
            if deposit <= 0:
                print("Deposit Amount must be a postive number")
                continue
            balance = balance + deposit
            print(f"Display balance after deposit - {balance}")

        case 3:
            print("user selected : Withdraw")
            amount = int(input("Enter amount to withdraw : "))
            if amount <= 0:
                print("Enter a positive number")
                continue
            elif amount > balance:
                print("Insufficient Balance")
            else:
                balance -= amount
                print(f"Available balance {balance} after withdrawal {amount}")
        case 4:
            print("user selected : Exit")
            break
        case _:
            print("Enter a valid option")
