logo = """
   ______                        __  __                                  __             
  / ____/_  _____  __________   / /_/ /_  ___     ____  __  ______ ___  / /_  ___  _____
 / / __/ / / / _ \/ ___/ ___/  / __/ __ \/ _ \   / __ \/ / / / __ `__ \/ __ \/ _ \/ ___/
/ /_/ / /_/ /  __(__  |__  )  / /_/ / / /  __/  / / / / /_/ / / / / / / /_/ /  __/ /    
\____/\__,_/\___/____/____/   \__/_/ /_/\___/  /_/ /_/\__,_/_/ /_/ /_/_.___/\___/_/     
                                                                                        
 """

from random import randint

easy_level = 10
hard_level = 5

# Function to check user's guess against actual answer
def check_answer(guess, answer, turns):
    """
    Checks answer against guess. Return the number of turns remaining.
    """
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You've got the number! The answer was {answer}. You win.")

# Function to set difficulty
def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == 'easy':
        return easy_level
    else:
        return hard_level


def game():
    # Choose a random number between 1 and 100
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)

    # Let the user guess a number
    turns = set_difficulty()

    # Repeat the guessing functionality if they get it wrong
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")

    # Let the user guess a number
        guess = int(input("Make a guess: "))

    # Track the number of turns and reduce by 1 they get it wrong
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses. You lose.")
            return
        elif guess != answer:
            print("Guess again.")


game()