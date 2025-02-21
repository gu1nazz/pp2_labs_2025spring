#1

def square_generator(n):
    for i in range(n+1):
        yield i ** 2

n = int(input("Enter a number N: "))

for square in square_generator(n):
    print(square, end=" ")

#2

def even_numbers(n):
    for num in range(n+1):
        if num % 2 == 0:
            yield num

n = int(input("Enter a number N: "))

print(",".join(str(num) for num in even_numbers(n)))

#3
def div_by_3_and_4(n):
    for i in range(n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input("Enter a number N: "))
print(list(div_by_3_and_4(n)))

#4

def squares(a, b):
    for i in range(a, b+1):
        yield i ** 2

a = int(input("Enter the starting number a: "))
b = int(input("Enter the ending number b: "))
print(list(squares(a, b)))

#5
def countdown(n):
    for i in range(n, -1, -1):
        yield i

n = int(input("Enter a number N: "))
print(list(countdown(n)))