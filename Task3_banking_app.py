def main():
    # 1. Initialize the opening balance with a fixed amount of 10,000
    balance = 10000
    
    print("Welcome to Kiran Bank")
    print(f"Opening Balance: ₹{balance}\n")
    
    # 2. Main menu loop that runs continuously until choice 4 is picked
    while True:
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        
        choice = input("Enter choice: ")
        
        # Step 2: Check balance
        if choice == '1':
            print(f"Current Balance: ₹{balance}\n")
            
        # Step 3: Deposit money
        elif choice == '2':
            try:
                deposit_amount = float(input("Enter deposit amount: "))
                # Validation: Amount must be greater than 0
                if deposit_amount > 0:
                    balance += deposit_amount
                    print("Deposit successful.")
                    print(f"Updated Balance: ₹{balance}\n")
                else:
                    print("Transaction failed: Amount must be greater than zero.\n")
            except ValueError:
                print("Invalid input! Please enter a numeric value.\n")
                
        # Step 4: Withdraw money
        elif choice == '3':
            try:
                withdraw_amount = float(input("Enter withdrawal amount: "))
                # Validation: Amount must be greater than 0
                if withdraw_amount <= 0:
                    print("Transaction failed: Amount must be greater than zero.\n")
                # Validation: Sufficient funds check
                elif withdraw_amount > balance:
                    print("Transaction failed: Insufficient balance.")
                    print(f"Current Balance: ₹{balance}\n")
                else:
                    balance -= withdraw_amount
                    print("Withdrawal successful.")
                    print(f"Updated Balance: ₹{balance}\n")
            except ValueError:
                print("Invalid input! Please enter a numeric value.\n")
                
        # Step 6: Exit program
        elif choice == '4':
            print("Thank you for banking with us. Goodbye!")
            break
            
        # Step 5: Handling invalid menu choices
        else:
            print("Invalid choice! Please select an option between 1 and 4.\n")

if __name__ == "__main__":
    main()
