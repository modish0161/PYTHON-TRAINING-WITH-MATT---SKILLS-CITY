import time
import random
import threading

# Constants
COUNTDOWN_TIME = 20

# Timer for displaying the remaining time during the quiz
def countdown_timer(remaining_time):
    while remaining_time > 0:
        time.sleep(1)
        remaining_time -= 1
    print("\nTime's up!")

# Function to display the quiz question and choices
def display_question(question_number, question):
    print(f"\nQuestion {question_number}: {question['question']}")
    for i, choice in enumerate(question['choices'], start=65):  # ASCII code for 'A' is 65
        print(f"{chr(i)}. {choice}")

# Function to get the user's answer
def get_user_answer():
    return input("Your answer (A/B/C/D): ").upper()

# Function to check if the user's answer is correct
def check_answer(user_answer, correct_answer):
    return user_answer == correct_answer[0]

# Prepare the quiz questions
questions = [
    {
        'question': "What is the capital of South Africa?",
        'choices': ["Nairobi", "Cape Town", "Johannesburg", "Pretoria"],
        'correct_answer': "Pretoria"
    },
        {
        'question': "What is the largest desert in Asia?",
        'choices': ["Gobi Desert", "Arabian Desert", "Karakum Desert", "Thar Desert"],
        'correct_answer': "Gobi Desert"
        },
        {
        'question': "Who invented the telephone?",
        'choices': ["Thomas Edison", "Alexander Graham Bell", "Nikola Tesla", "Michael Faraday"],
        'correct_answer': "Alexander Graham Bell"
        },
    # Add more questions...
]

# Shuffle the questions to present them in a random order
random.shuffle(questions)

# Display instructions
print("Welcome to the Interactive Quiz Game!")
print("You will be presented with a series of questions. Choose the correct option.")

# Iterate through the questions
score = 0

for idx, question in enumerate(questions, start=1):
    display_question(idx, question)

    # Set initial remaining time
    remaining_time = COUNTDOWN_TIME

    # Start the countdown timer in a separate thread
    timer_thread = threading.Thread(target=countdown_timer, args=(remaining_time,))
    timer_thread.start()

    print(f"\nTime Allowed: {COUNTDOWN_TIME:.2f} seconds")
    user_answer = get_user_answer()

    # Stop the countdown timer thread
    timer_thread.join()

    elapsed_time = min(COUNTDOWN_TIME - remaining_time, COUNTDOWN_TIME)

    if user_answer in ['A', 'B', 'C', 'D'] and check_answer(user_answer, question['correct_answer']):
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer is {question['correct_answer']}.")

    print(f"Time taken: {elapsed_time:.2f} seconds")
