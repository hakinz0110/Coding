print("Welcome to Treasure Island")
print("your mission is to find the treasure.")

choice1 = input('You\'re at a crossroad, where do you want to go? Type "left" or "right". \n').lower()

if choice1 == "left":
  choice2 = input('You\'av come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
  if choice2 == "wait":
    #game continue
    choice3 = input(" You arrive at the island unhammed. There is a house with 3 doors. One red, one yellow, and one blue. Which colour do you choose? \n").lower()
    if choice3 == "red":
      print("It's a room full of fire. Game over.")
    elif choice3 == "yellow":
      print("You found the treasure! You WIN!")
    elif choice3 == "blue":
      print("You enter a room full of beasts. Game Over.")
    else:
      print("You chose a door that doesn't exist. Game Over.")
  else:
    print("You got attacked by an angry trout. GAME OVER.")
else:
  print("You fell into a hole. GAME OVER.")