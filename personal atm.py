account ={
    "name": "John",
    "balance": "10000",
    "pin": "3345",
    "ac type":"bussinessaccount"
}
print("===MINI ATM===")
pin = input("Enter your pin:")
if pin == account["pin"]:
    while True:
        print("===ATM MENU===")
        print("1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Account Details")
        print("5. Exit")
        choice = input("Enter your choice:")

        if choice == "1":
            print("Your balance is:", account["balance"])

        elif choice == "2":
            amount = int(input("Enter amount to withdraw:"))
            if amount <= int(account["balance"]):
                account["balance"] = str(int(account["balance"]) - amount)
                print("Withdrawal successful. New balance is:", account["balance"])
            else:
                print("Insufficient balance.")


        elif choice == "3":
            amount = int(input("Enter amount to deposit:"))
            account["balance"] = str(int(account["balance"]) + amount)
            print("Deposit successful. New balance is:", account["balance"])

        elif choice == "4":
            print("Account Details:")
            print("Name:", account["name"])
            print("Account Type:", account["ac type"])
            print("Balance:", account["balance"])


        elif choice == "5":
            print("Thank you for using the ATM.")
            break
        else:
            print("Invalid choice. Please try again.")



