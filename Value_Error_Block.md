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

The try block attempts to convert the user's input into a floating-point number using float(). If the user enters something that is not a valid numerical value (for example, a string or a non-numeric character), a ValueError will be raised. The except ValueError block catches this exception and prints an error message indicating that the input is invalid.

This helps handle cases where the user enters something that cannot be converted into a valid numerical value, preventing the program from crashing due to an unexpected input type.