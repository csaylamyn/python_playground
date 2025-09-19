import random

# Function to run a single round of the game
def play_game():
    secret_number = random.randint(1, 10)
    guesses = 0
    guessed_correctly = False

    print("I'm thinking of a number between 1 and 10. Can you guess it?")

    while not guessed_correctly:
        try:
            guess = int(input("Enter your guess: "))
            guesses += 1

            # Use match-case with conditional guards for all comparisons
            match guess:
                case _ if guess < secret_number:
                    print("Nope, your guess is a bit low. Give it another shot!")
                case _ if guess > secret_number:
                    print("Oops, your guess is a bit high. Try again!")
                case _:
                    # The only remaining possibility is that the guess is correct
                    print(f"Congratulations, you guessed it in {guesses} attempts!")
                    guessed_correctly = True

        except ValueError:
            print("Invalid input. Please enter a whole number.")

# Main game loop for playing again
def main():
    play_again = 'yes'
    while play_again.lower() == 'yes':
        play_game()
        play_again = input("Play again? (yes/no)\n")

    print("Thanks for playing!")

# Run the game
if __name__ == "__main__":
    main()

