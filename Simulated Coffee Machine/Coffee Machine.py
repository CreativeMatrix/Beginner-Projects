MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.00,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def check_resources(ingredients):
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

def calculate_coins():
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def checkout(payment, drink_cost):
    if payment == drink_cost:
        return True
    elif payment < drink_cost:
        print("Sorry, that is not enough Money, your Money has been refunded.")
    elif payment > drink_cost:
        user_change = payment - drink_cost
        round(user_change)
        print(f"Here is ${user_change}0 in change.")
        return True

money = 0
coffeemaker_is_on = True
while coffeemaker_is_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == 'off':
        coffeemaker_is_on = False
    elif user_choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    elif user_choice == 'espresso':
        print(f"The Espresso costs ${MENU['espresso']['cost']}0")
        drink = MENU["espresso"]
        if check_resources(drink['ingredients']):
            payment = calculate_coins()
            if checkout(payment, MENU['espresso']['cost']):
              resources['water'] -= MENU["espresso"]['ingredients']['water']
              resources['coffee'] -= MENU["espresso"]['ingredients']['coffee']
              money += MENU['espresso']['cost']
              print("Enjoy your Espresso!") 
    elif user_choice == 'latte':
        print(f"The Latte costs ${MENU['latte']['cost']}0")
        drink = MENU["latte"]
        if check_resources(drink['ingredients']):
            payment = calculate_coins()
            if checkout(payment, MENU['latte']['cost']):
              resources['water'] -= MENU["latte"]['ingredients']['water']
              resources['coffee'] -= MENU["latte"]['ingredients']['coffee']
              resources['milk'] -= MENU["latte"]['ingredients']['milk']
              money += MENU['latte']['cost']
              print("Enjoy your Latte!")   
    elif user_choice == 'cappuccino':
        print(f"The Cappuccino costs ${MENU['cappuccino']['cost']}0")
        drink = MENU["cappuccino"]
        if check_resources(drink['ingredients']):
            payment = calculate_coins()
            if checkout(payment, MENU['cappuccino']['cost']):
              resources['water'] -= MENU["cappuccino"]['ingredients']['water']
              resources['coffee'] -= MENU["cappuccino"]['ingredients']['coffee']
              resources['milk'] -= MENU["cappuccino"]['ingredients']['milk']
              money += MENU['cappuccino']['cost']
              print("Enjoy your Cappuccino!")  
