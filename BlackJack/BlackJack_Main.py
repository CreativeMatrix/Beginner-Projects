import random
from tkinter import Y
from art import logo
import os

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards)
    return random_card

def calculate_score(score):
    cards_sum = sum(score)
    return cards_sum

def play_game():
    print(logo)
    user_cards = []
    dealer_cards = []
    for _ in range(2):
        user_cards.append(deal_card())
        dealer_cards.append(deal_card())
    
    continue_game = True
    while continue_game:
        user_score = calculate_score(user_cards)
        dealer_score = calculate_score(dealer_cards)
        print(f'Your Cards: {user_cards}, Current Score: {user_score}')
        print(f"Dealer's First Card: {dealer_cards[0]}")
        if user_score == 21:
            print("You Win!")
            continue_game = False
            break
        elif user_score > 21 and 11 not in user_cards:
             print("BUST! You Lose!")
             continue_game = False
             break
        elif user_score > 21 and 11 in user_cards:
            user_cards.remove(11)
            user_cards.append(1)
            print(f"You went over 21, but you have an ACE [11]. This card will be changed to [1].")
            print(f"Your NEW Cards: {user_cards}, Current NEW Score: {calculate_score(user_cards)}")
    
        another_card = input("Type 'Y' to get another card, type 'N' to pass: ").lower()
        os.system('cls')
        print(logo)
        if another_card == "y":
            user_cards.append(deal_card())
        elif another_card == "n":
            dealer_turn = True
            while dealer_turn:
                print(f'Your Cards: {user_cards}, Current Score: {calculate_score(user_cards)}')
                print(f"Dealer's Cards: {dealer_cards}, Dealer Score: {calculate_score(dealer_cards)}")
                if calculate_score(dealer_cards) == 21:
                    print("Dealer Wins!")
                    dealer_turn = False
                    continue_game = False
                elif calculate_score(dealer_cards) > 21 and 11 in dealer_cards:
                    input(f"Dealer went over 21, but has the ACE [11]. This card will be changed to [1]. Hit 'Enter' to continue: ")
                    dealer_cards.remove(11)
                    dealer_cards.append(1)
                    os.system('cls')
                    print(logo)
                elif calculate_score(dealer_cards) < user_score and calculate_score(dealer_cards) < 21:
                    input("Dealer has not gone over. Dealer will add another card. Type 'Enter' to continue: ")
                    dealer_cards.append(deal_card())
                    os.system("cls")
                    print(logo)
                    continue
                elif calculate_score(dealer_cards) > user_score and calculate_score(dealer_cards) < 21:
                    print("Dealer Wins!")
                    dealer_turn = False
                    continue_game = False
                elif calculate_score(dealer_cards) > 21:
                    print('Dealer BUST! You Win!')
                    dealer_turn = False
                    continue_game = False
                elif calculate_score(dealer_cards) == user_score:
                    print("It's a DRAW!")
                    dealer_turn = False
                    continue_game = False
    play_again = input("Do you want to play another game of BlackJack? Type 'Y' or 'N' to continue. ").lower()
    if play_again == 'y':
        os.system('cls')
        play_game()
    else:
        print("Thanks for playing!")
    return "Game Over."            
    
print(logo)         
play_blackjack = input("Do you want to play a game of black jack? Type 'Y' or 'N': ").lower()
if play_blackjack == 'y':
    os.system('cls')
    play_game()
else:
    os.system('cls')
    print(logo)
    print("Game Over!")


