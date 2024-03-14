# Make a rock paper scissors app that I can play against the computer. 
# The program should keep track of the number of rounds played, the number of rounds
# won by the user, and the number of rounds won by the computer. 
# After each round, the program should display the results 
# and ask the user if they want to play another round. 
# You should use functions, loops, conditionals, random number generation to achieve this.

def play_round():
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)  # Use the random module to select a choice for the computer
    user_choice = input("Enter your choice (rock/paper/scissors): ")
    print(f"Computer chose: {computer_choice}")

    if user_choice.lower() == computer_choice:
        return "tie"
    elif user_choice.lower() == "rock":
        # Complete the condition and return value
    elif user_choice.lower() == "paper":
        # Complete the logic for when the user chooses paper
    elif user_choice.lower() == "scissors":
        # Complete the logic for when the user chooses scissors
    else:
        print("Invalid choice. Please try again.")
        return play_round() 

num_rounds = 0
user_wins = 0
computer_wins = 0
play_again = "y"

while play_again.lower() == "y":
    num_rounds += 1
    result = play_round()
    if result == "user":
        user_wins += 1
        print("You win!")
    elif result == "computer":
        computer_wins += 1
        print("Computer wins!")
    else:
        print("Tie game.")
    print(f"Rounds played: {num_rounds}")
    print(f"User wins: {user_wins}")
    print(f"Computer wins: {computer_wins}")
    play_again = input("Play another round? (y/n) ")