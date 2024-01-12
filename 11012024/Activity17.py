import random

# List of cards
cards = ["Diamond", "Spade", "Club", "Heart"]

# Card to find
target_card = "Spade"

# Variable to store the current card
current_card = None

# Keep looping until the current card matches the target card
while current_card != target_card:
    # Randomly choose a card from the list
    current_card = random.choice(cards)
    
    # Print the current card for visual (optional)
    print("Current Card:", current_card)
    
# Print a message when the target card is found
print(f"Found the target card '{target_card}'!")