import random
print("Welcom to the PyPassword Generator!")
num_letters = int(input("How many letters would you like in your password? \n"))
num_symbols = int(input("How many numbers would you like? \n"))
number_numbers = int(input("how many numbers would you like? \n"))

letters = [ "a", "b", "c", "c", "d", "e", "f", "g", "h", "i", "j", "k",
"l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w",
"x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I",
"J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
"V", "W", "X", "Y", "Z" ]

numbers = [ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' ]
symbols = [ '!', '@', '#', '$', '%', '^', '&', '*', '_', '~', '?' ]
 
password = ""
for char in range(1, num_letters + 1):
  random_char = random.choice(letters)
  password += random_char

for char in range(1, num_symbols + 1):
  random_char = random.choice(symbols)
  password += random_char
  
for char in range(1, num_symbols + 1):
  random_char = random.choice(numbers)
  password += random_char
print(password)


print("OR")
  
    
password_list = []
for char in range(1, num_letters + 1):
  password_list.append(random.choice(letters))

for char in range(1, num_symbols + 1):
 password_list.append(random.choice(symbols))

for char in range(1, number_numbers + 1):
  password_list.append(random.choice(numbers))

print(password_list) 
  
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
  password += char
print(password)