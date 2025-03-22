def all_elements_true(my_tuple):
    return all(my_tuple)

# Get input from the user
user_input = input("Enter tuple elements separated by space: ")

# Convert input string to a tuple (all elements are strings)
my_tuple = tuple(user_input.split())

# Check and display result
result = all_elements_true(my_tuple)
print("Are all elements true?:", result)

#(True, 1, "Сәлем", 5.5)