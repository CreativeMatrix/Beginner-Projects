import numbers
import random
from art import logo

print(logo)
print("Welcome to The Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
user_difficulty = input("Choose a difficulty. Type 'Easy' or 'Hard' to start: ").lower()
hidden_number = random.randint(1, 100)


def easy_game():
    number_of_attempts = 10
    while number_of_attempts > 0:
        print(f"You have {number_of_attempts} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        if user_guess == hidden_number:
            print(f"You have successfully guessed the correct number which is {hidden_number}. You Win!")
            break
        elif user_guess != hidden_number:
            if user_guess > hidden_number:
                number_of_attempts -= 1
                if number_of_attempts == 0:
                    print("You have ran out of attempts.")
                    break  
                print("To High.\nGuess again please.")
            elif user_guess < hidden_number:
                number_of_attempts -= 1
                if number_of_attempts == 0:
                    print("You have ran out of attempts.")
                    break  
                print("To Low.\nGuess again please.")
    print("Game Over! Thanks for playing!")
                


def hard_game():
    number_of_attempts = 5
    while number_of_attempts > 0:
        print(f"You have {number_of_attempts} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        if user_guess == hidden_number:
            print(f"You have successfully guessed the correct number which is {hidden_number}. You Win!")
            break
        elif user_guess != hidden_number:
            if user_guess > hidden_number:
                number_of_attempts -= 1
                if number_of_attempts == 0:
                    print("You have ran out of attempts.")
                    break  
                print("To High.\nGuess again please.")
            elif user_guess < hidden_number:
                number_of_attempts -= 1
                if number_of_attempts == 0:
                    print("You have ran out of attempts.")
                    break  
                print("To Low.\nGuess again please.")
    print("Game Over! Thanks for playing!")


if user_difficulty == 'easy':
    easy_game()
elif user_difficulty == 'hard':
    hard_game()
