print("ATM BANKING SYSTEM")

balance = 1000.0
transactions = []

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Transaction Summary")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter deposit amount: "))
        if amount <= 0:
            print("Invalid deposit amount")
        else:
            balance += amount
            transactions.append(("Deposit", amount))
            print("Deposit successful")

    elif choice == "2":
        amount = float(input("Enter withdrawal amount: "))
        if amount <= 0:
            print("Invalid withdrawal amount")
        elif amount > 10000:
            print("Withdrawal limit exceeded")
        elif amount > balance:
            print("Insufficient balance")
        else:
            balance -= amount
            transactions.append(("Withdrawal", amount))
            print("Withdrawal successful")

    elif choice == "3":
        print("Current Balance: Rs.", balance)

    elif choice == "4":
        print("\nTRANSACTION SUMMARY")
        if not transactions:
            print("No transactions yet.")
        for transaction_type, amount in transactions:
            print(transaction_type, ": Rs.", amount)
        print("Final Balance: Rs.", balance)

    elif choice == "5":
        print("Thank you for using the ATM")
        break

    else:
        print("Invalid choice")
