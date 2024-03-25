import random
  
lives = 6
end_of_game = False
word_list = ["hell", "welcome", "mum", "to", "engine", "force", "momentum"]
chosen_word = random.choice(word_list)
word_lenght = len(chosen_word)

#create blanks
display = []
for _ in chosen_word:   ## for _ in range(len(chosen_word)):
  isplay += "_"


while not end_of_game:  
  guess = input("Guess a letter: ").lower()

  #Check geussed leter
  for position in range (word_lenght):
    letter = chosen_word[position]
    if letter == guess:
      display[position] = letter
    
  print(display)
  
  if "_" not in display:
    end_of_game = True
    print("You Win!!!.")
    
    
# for letter in chosen_word:
#   if letter == guess:
#     print("Right")
#   else:
#     print("Wrong")
# print(chosen_word)


 