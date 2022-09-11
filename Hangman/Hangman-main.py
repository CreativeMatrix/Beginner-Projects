import random
from hangman_art import stages, logo
from hangman_words import word_list


print(logo)
chosen_word = random.choice(word_list)
lives = 7

display = []
for index in chosen_word:
  display.append("_")
print(f"{' '.join(display)}")
  
letters_guessed = []
while "_" in display:
  guess = input("Guess a letter: ").lower()
  if guess in letters_guessed:
        print(f"You have already chosen the letter: '{guess}'\nPlease choose another letter!")
  letters_guessed.append(guess)

  for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
      display[position] = letter
  if guess not in chosen_word:
      lives -= 1
      print(f"The letter you've chosen: '{guess}' is not in the word.\nPlease choose another letter!")

  if lives == 6:
      print(stages[6])
  elif lives == 5:
      print(stages[5])
  elif lives == 4:
      print(stages[4])
  elif lives == 3:
      print(stages[3])
  elif lives == 2:
      print(stages[2])
  elif lives == 1:
      print(stages[1])
  elif lives == 0:
      print(f"{stages[0]}\nYou Lose! The word is {chosen_word}.")


  print(f"{lives} Lives available.")
  print(f"{' '.join(display)}")
print("You Win!")

