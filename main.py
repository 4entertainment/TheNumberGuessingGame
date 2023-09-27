from art import logo
import random


def difficulty(choose):
    if choose == 'hard':
        attempts = 5
        return attempts
    elif choose == 'easy':
        attempts = 10
        return attempts


def get_number():
    number = random.randint(1, 100)
    return number


def game_on():
    print("Welcome to the Number Guessing Name!\nI'm thinking of a number between 1 and 100.")
    chosen_number = get_number()
    attempts = difficulty(input("Choose a difficulty. Type 'easy' or 'hard': "))
    print(f"You have {attempts} attempts remaining to guess the number.")

    while attempts > 0:
        guess = int(input("Make a guess: "))
        if guess > chosen_number:
            print("Too high.")
            attempts -= 1
        elif guess < chosen_number:
            print("Too low.")
            attempts -= 1
        elif guess == chosen_number:
            print(f"You got it! The answer was {chosen_number}.")
            break
        print(f"Guess again.\nYou have {attempts} attempts remaining to guess the number.")

    if attempts == 0:
        print("You've run out of guesses, you lose.")


print(logo)

game_on()





