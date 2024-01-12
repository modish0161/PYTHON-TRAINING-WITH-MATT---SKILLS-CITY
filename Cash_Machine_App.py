# Cash Machine App

# Set the PIN and initial balance
correct_pin = "1234"
initial_balance = 1000

# Prompt the user to enter the PIN
user_pin = input("Enter your PIN: ")

# Check if the entered PIN is correct
if user_pin == correct_pin:
    # PIN is correct
    print("Welcome to the Cash Machine!")
    
    # Display the initial balance
    print("Your current balance: £{}".format(initial_balance))
    
    # Prompt the user to withdraw cash
    try:
        withdrawal_amount = float(input("Enter the amount to withdraw: £"))
        
        # Check if the withdrawal amount is valid
        if withdrawal_amount <= initial_balance:
            # Update the balance
            remaining_balance = initial_balance - withdrawal_amount
            
            # Display success message and remaining balance
            print("Withdrawal successful! Remaining balance: £{}".format(remaining_balance))
        else:
            print("Insufficient funds. Please enter a valid amount.")
    
    except ValueError:
        print("Invalid input. Please enter a valid numerical amount.")
    
else:
    # Incorrect PIN
    print("Incorrect PIN. Access denied.")
