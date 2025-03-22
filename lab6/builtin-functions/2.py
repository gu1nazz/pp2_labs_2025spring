def count_letters(text):
    upper = sum(1 for char in text if char.isupper())
    lower = sum(1 for char in text if char.islower())

    print("Uppercase letters:", upper)
    print("Lowercase letters:", lower)

sentence = input("Enter a sentence: ")
count_letters(sentence)