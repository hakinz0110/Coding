import random

namesAsCSV = input("Give me evebody's names, separated by a comma. \n")
names = namesAsCSV.split(", ") # this convert the input name into list data
# get the total number of items in the list
name_lenght = len(names)
# generate random numbers between 0 and the last index
choice_person = random.randint(0, name_lenght - 1)
who_is_paying = names[choice_person]
print(f"{who_is_paying} is paying for the meal today")