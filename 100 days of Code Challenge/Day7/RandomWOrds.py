import random
  
word_list = ["hello", "welcom", "museum", "rain", "engine", "skin", "before", "odor", "visa", "rebel", "shove", "female", "alpha", "dwarf"]

chosen_word = random.choice(word_list)

display = []
for _ in chosen_word:   ## for _ in range(len(chosen_word)):
  display += "_"
print(display)

guess = input("Guess a letter: ").lower()
word_lenght = len(chosen_word
for position in (word_lenght)):
  letter = chosen_word[position]
  if letter == guess:
    display[position] = letter
# for letter in chosen_word:
#   if letter == guess:
#     print("Right")
#   else:
#     print("Wrong")
# print(chosen_word)