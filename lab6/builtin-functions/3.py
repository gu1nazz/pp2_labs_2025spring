def is_palindrome(text):
    return text == text[::-1]

sentence = input("Enter a sentence: ")
if is_palindrome(sentence):
    print("The string is a palindrome.")
else:
    print("The string is NOT a palindrome.")