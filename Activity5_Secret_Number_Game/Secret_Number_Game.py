# Secret number
secret_number = 7

# Prompt the user to guess the secret number
while True:
    try:
        guess = int(input("Guess the secret number (between 1 and 10): "))
        
        if guess == secret_number:
            print("Congratulations! You got the number correct.")
            break
        else:
            print("Incorrect. Please, Try again!")
    except ValueError:
        print("Invalid input. Please enter a valid number.")