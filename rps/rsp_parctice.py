# Step 1: Import the random module to generate a random choice for the computer.
# (Hint: Use "import random")
import random

# Step 2: Create a list containing the three possible choices: "rock", "paper", "scissors"
# (Hint: Use a list like this: ["rock", "paper", "scissors"])
choices = ["rock","paper","scissors"]
# Step 3: Define a function to determine the winner.
# - It should take two parameters: the player's choice and the computer's choice.
def get_winner(player,computer):
    """
    Determines the winner based on the game rules.
    """
    if player == computer:
        return "It's a tie!"
# - If both choices are the same, return "It's a tie!"
    elif(player == "rock" and computer == "scissors") or (player == "scissors" and computer == "paper") or (player == "paper" and computer == "rock"):
        return "You win!"
# - If the player wins based on the rules, return "You win!"
    else:return "Computer wins"
# - Otherwise, return "Computer wins!"
# (Hint: Use an if-elif-else statement to compare choices)

# Step 4: Create a function to run the game.
def play_game():
    """
    Runs the rock-paper-sissors game in a loop until
    the players chooses to quit
    """
# - Start an infinite loop using "while True"
    while True:
        print("\nRock, Paper, Scissors!")
        # - Ask the player to input their choice (rock, paper, or scissors)
        players_choice = input("Enter your choice:rock,paper, or scissors (or 'quit' to exit) ").lower()
        # - Convert the input to lowercase to ensure case insensitivity
        if players_choice == "quit":
            print("Thank you for playing!")
            break
# - If the player types "quit", print a goodbye message and break the loop
        if players_choice not in choices:
            print("Invalid choice. Please try again.")
            continue
# - If the input is not valid, prompt the user again
# - The computer should randomly select a choice from the list
        computer_choice = random.choice(choices)
        print(f"Computer's choice: {computer_choice}")
# - Print both the player's and computer's choices
# - Call the function that determines the winner and print the result
        result = get_winner(players_choice,computer_choice)
        print(result)
# Step 5: Call the function to start the game.
play_game()