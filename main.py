from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# Check user answer
def check_answer(guess, answer, turns):
    '''Checks answer against guess. Returns the number of turns remaining.'''
    if guess > answer:
        print("Too High!")
        return turns - 1
    elif guess < answer:
        print("Too Low!")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")

# Set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

# Set the Game
def game():
    print(logo)
    # Choosing a number between 1 and 100.abs
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    #test piece (take out when done testing)
    print(f"pssst... the correct answer is {answer}.")
    # Set the number of turns
    turns = set_difficulty()
    # Set the guess
    guess = 0
    # Loop until the guess is correct or player looses
    while guess != answer:
        print(f"You have {turns} guesses remaining.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses. You Lose.")
            print(f"The correct number was {answer}.")
            return
        elif guess != answer:
            print("Guess again.")

game()
