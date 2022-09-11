from art import logo, vs
from game_data import data
import random
import os


user_score = 0
continue_game = True
celebrity_b = random.choice(data)

while continue_game:
    celebrity_a = celebrity_b
    celebrity_b = random.choice(data)
    if celebrity_a == celebrity_b:
        continue
    
    print(logo)
    print(f"Celebrity A: {celebrity_a['name']}, who is a {celebrity_a['description']}, from {celebrity_a['country']}.")
    print(vs)
    print(f"Celebrity B: {celebrity_b['name']}, who is a {celebrity_b['description']}, from {celebrity_b['country']}.")
    followers_a = celebrity_a['follower_count']
    followers_b = celebrity_b['follower_count']
    
    user_choice = input(f"Who has more followers? Type 'A' for {celebrity_a['name']} or 'B' for {celebrity_b['name']}: ").lower()
    if user_choice == 'a':
        compare = followers_a > followers_b
        if compare == True:
            user_score += 1
            os.system('cls')
            print(f"You're right! Current score: {user_score}")
        elif compare == False:
            continue_game = False
    elif user_choice == 'b':
        compare = followers_b > followers_a
        if compare == True:
            user_score += 1
            os.system('cls')
            print(f"You're right! Current score: {user_score}")
        elif compare == False:
            continue_game = False

os.system('cls')
print(logo)
print(f"Sorry, that's incorrect. Final score: {user_score}")    