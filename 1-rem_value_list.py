# How to remove value from list 
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Remove specific value from list using index number

rem_value = numbers.pop(3)
print(rem_value)

# remove last item from list

numbers.pop()
print(numbers)

# Remove value by name

numbers.remove(8)
print(numbers)