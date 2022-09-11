import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

user_letter = []
user_password = ""
for letter in range(nr_letters):
  user_letter.append(letters[letter])

for symbol in range(nr_symbols):
  user_letter.append(symbols[symbol])

for number in range(nr_numbers):
  user_letter.append(numbers[number])

for user in user_letter:
  user_password += user

print(f"Here is your password: {user_password}")
  

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

user_letter = []
user_password = ""

for letter in range(nr_letters):
  random_letter = random.choice(letters)
  user_letter.append(random_letter)

for symbol in range(nr_symbols):
  random_symbol = random.choice(symbols)
  user_letter.append(random_symbol)

for number in range(nr_numbers):
  random_number = random.choice(numbers)
  user_letter.append(random_number)

random.shuffle(user_letter)
for user in user_letter:
  user_password += user

print(f"Here is your password: {user_password}")