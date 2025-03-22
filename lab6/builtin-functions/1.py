input_numbers = input("Enter space-separated numbers: ")
number_list = list(map(int, input_numbers.split()))

product = 1
for number in number_list:
    product *= number

print("Product of all numbers:", product)