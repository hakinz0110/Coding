sum_evens = 0
for numbers in range(0, 101, 2):
  sum_evens += numbers
print(sum_evens)




sum_evens = 0
for numbers in range(1, 101):
  if numbers % 2 ==  0:
    sum_evens += numbers
print(sum_evens)