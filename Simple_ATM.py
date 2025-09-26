print("Welcome to the ATM")
Password = "1234"
Balance = 1000
Attempts = 3
while Attempts > 0:
    Pin = input("Enter your PIN: ")
    if Pin == Password:
        print("Access Granted")
        while True:
            print("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit")
            choice = input("Choose an option: ")
            if choice == '1':
                print(f"Your balance is: ${Balance}")
            elif choice == '2':
                amount = float(input("Enter amount to deposit: "))
                if amount > 0:
                    Balance += amount
                    print(f"${amount} deposited. New balance is: ${Balance}")
                else:
                    print("Invalid amount.")
            elif choice == '3':
                amount = float(input("Enter amount to withdraw: "))
                if 0 < amount <= Balance:
                    Balance -= amount
                    print(f"${amount} withdrawn. New balance is: ${Balance}")
                else:
                    print("Invalid amount or insufficient funds.")
            elif choice == '4':
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")
        break
    else:
        Attempts -= 1
        print(f"Incorrect PIN. You have {Attempts} attempts left.")
        if Attempts == 0:
            print("Account locked due to too many incorrect attempts.")