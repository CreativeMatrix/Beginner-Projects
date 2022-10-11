from os import system
from art import logo

print(logo)
print("Hello and Welcome to the Secret Aution!")

user_prices = {}
continue_bid = True
while continue_bid:
    user_name = input("What is your Name? ")
    user_bid = int(input('What is your Bid? $'))
    user_prices[user_name] = user_bid

    next_bid = input("Are there any other bidders? Type 'Yes' or 'No'. ").lower()
    if next_bid == "yes":
        _ = system('cls')
        continue_bid
    elif next_bid == "no":
        continue_bid = False


max_value = max(user_prices.values())
max_key = max(user_prices, key = user_prices.get)
print(f"{max_key} has the highest bid with ${max_value} dollars!")

