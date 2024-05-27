# create a game called "Rock, Paper, Scissors" using Python.

# Create a user option to select rock, paper, or scissors
# Create a computer option to randomly select rock, paper, or scissors
# Compare the user and computer selections
# Determine the winner
# Display the results
# Allow the user to play again



import random

print("Welcome to Rock, Paper, Scissors!")
print("You will be playing against the computer.")

while True:
    user = input("Select 'r' for rock, 'p' for paper, or 's' for scissors: ")
    while user not in ['r', 'p', 's']:
        print("Invalid selection. Please try again.")
        user = input("Select 'r' for rock, 'p' for paper, or 's' for scissors: ")

    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        print("It's a tie!")
    elif user == 'r' and computer == 's':
        print("You win! Rock beats scissors.")
    elif user == 'p' and computer == 'r':
        print("You win! Paper beats rock.")
    elif user == 's' and computer == 'p':
        print("You win! Scissors beats paper.")
    else:
        print("You lose!")

    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() != 'y':
        break

print("Thanks for playing!")