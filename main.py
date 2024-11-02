import random # Imports the random module to generate a random number
from art import logo, you_lose_logo, logo_end # Imports logos from the art module

# Function to play the game in 'easy' mode with 10 attempts
def play_easy():
    count = 10 # Set initial attempt count for easy mode

    should_continue = True # Variable to control loop continuation
    while should_continue:
        # Check if the user has run out of guesses
        if count < 1:
            print(you_lose_logo) # Print losing logo if attempts are exhausted
            print("You have run out of guesses")
            print(f"The Number was: {random_number}.\nSorry try again next time lol...")
            break # Exit the loop if attempts are finished

        print(f"You have {count} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: ")) # Prompt user to guess
        # Provide feedback based on the guessed number
        if user_guess < random_number:
            print("Too Low.")
            print("Guess again.")
            count -= 1  # Decrease attempt count for an incorrect guess
            continue
        elif user_guess > random_number:
            print("Too High.")
            print("Guess again.")
            count -= 1  # Decrease attempt count for an incorrect guess
            continue
        elif user_guess == random_number:
            print(f"You guessed it, the answer was {random_number}.") # Correct guess message
            should_continue = False # Exit the loop as the user has guessed correctly

# Function to play the game in 'hard' mode with 5 attempts
def play_hard():
    count = 5 # Set initial attempt count for hard mode

    should_continue = True # Variable to control loop continuation
    while should_continue:
        # Check if the user has run out of guesses
        if count < 1:
            print(you_lose_logo) # Print losing logo if attempts are exhausted
            print("You have run out of guesses")
            print(f"The Number was: {random_number}.\nSorry try again next time lol...")
            break  # Exit the loop if attempts are finished


        print(f"You have {count} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))  # Prompt user to guess

        # Provide feedback based on the guessed number
        if user_guess < random_number:
            print("Too Low.")
            print("Guess again.")
            count -= 1  # Decrease attempt count for an incorrect guess
            continue
        elif user_guess > random_number:
            print("Too High.")
            print("Guess again.")
            count -= 1  # Decrease attempt count for an incorrect guess
            continue
        elif user_guess == random_number:
            print(f"You guessed it, the answer was {random_number}.") # Correct guess message
            should_continue = False   # Exit the loop as the user has guessed correctly




# Main function to start the game based on chosen difficulty
def play_game(user_difficulty):
    if user_difficulty == "easy":
        play_easy() # Start the easy mode game
    elif user_difficulty == "hard":
        play_hard() # Start the hard mode game

# Display the game logo and initial message
print(logo)
random_number = random.randint(1,100)  # Generate a random number between 1 and 100
print("Welcome to the Number Guessing Game!!")
print("I'm thinking of a number between 1 and 100.")
user_choice = input("Choose a Difficulty, 'easy' or 'hard': ").lower()  # Prompt user for difficulty

play_game(user_choice)  # Start the game with chosen difficulty

# Loop to allow the player to restart the game if they wish
play_again = True
while play_again:
    game_start_repeat = input("Do you want to play the number guessing game again, Type 'y' or 'n': ").lower()
    if game_start_repeat == "y":
        print("\n" * 1000) # Clear the screen
        print(logo)
        random_number = random.randint(1, 100) # Generate a new random number for the new game
        print("Welcome to the Number Guessing Game!!")
        print("I'm thinking of a number between 1 and 100.")
        user_choice = input("Choose a Difficulty, 'easy' or 'hard': ").lower()

        play_game(user_choice)  # Start a new game based on chosen difficulty

    elif game_start_repeat == "n":
        print(logo_end) # Print ending logo when the game finishes
        print("Thanks for playing!!, we hope you had a fun time\nBye!!")
        play_again = False  # End the loop if the user chooses not to play again



