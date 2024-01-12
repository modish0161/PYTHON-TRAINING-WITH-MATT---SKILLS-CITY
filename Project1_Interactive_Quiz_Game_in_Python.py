import time
import random  # Import the 'random' module to shuffle questions

# Define the list of questions
questions = [
    # Your list of questions goes here
]

# Shuffle the questions to present them in a random order
random.shuffle(questions)


# Step 1: Set up the project

# Create a new Python file named 'quiz_game.py' and open it in your preferred code editor.

# Step 2: Prepare the quiz questions

# Define a list of questions, each with a statement and multiple choices, including one correct answer.
# Add more questions with no duplicates to reach the desired count (50 in this case).

# Step 3: Display instructions

# Print a welcome message and instructions for the quiz game.
print("Welcome to the Interactive Quiz Game!")
print("You will be presented with a series of questions. Choose the correct option.")

# Step 4: Iterate through the questions

# Initialize the score
score = 0

# Iterate through each question in the list and present it to the user
for idx, question in enumerate(questions, start=1):
    # Display the question statement
    print(f"\nQuestion {idx}: {question['question']}")
    
    # Display the answer choices
    for i, choice in enumerate(question['choices'], start=65):  # ASCII code for 'A' is 65
        print(f"{chr(i)}. {choice}")

    # Step 7: Add a timer
    countdown = 30  # Set the countdown time to 30 seconds
    start_time = time.time()

    user_answer = input("\nYour answer (A/B/C/D): ").upper()
    end_time = time.time()

    # Check if the user answered before the countdown ends
    elapsed_time = end_time - start_time
    remaining_time = max(countdown - elapsed_time, 0)
    if remaining_time == 0:
        print("Time's up!")
    else:
        print(f"Time left: {remaining_time:.2f} seconds")

    # Step 5: Check the answer
    if user_answer == question['correct_answer'][0]:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer is {question['correct_answer']}.")

# Step 6: Display the result

# Print the final score at the end of the quiz
print("\nQuiz completed!")
print(f"Your final score is: {score} out of {len(questions)}.")

# End of the quiz game
