import random
import math



def reverse_words(sentence):
    return ' '.join(sentence.split()[::-1])

def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

def spy_game(nums):
    code = [0, 0, 7]
    for num in nums:
        if num == code[0]:
            code.pop(0)
        if not code:
            return True
    return False

def sphere_volume(radius):
    return (4/3) * math.pi * radius**3

def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

def histogram(lst):
    for num in lst:
        print('*' * num)
def main():
    print("Testing functions:\n")
    
    # Test reverse_words
    sentence = "We are ready"
    print("Reversed words:", reverse_words(sentence))
    
    # Test has_33
    num_list = [1, 3, 3]
    print("Contains consecutive 3s:", has_33(num_list))
    
    # Test spy_game
    spy_list = [1, 2, 4, 0, 0, 7, 5]
    print("Contains 007 in order:", spy_game(spy_list))
    
    # Test sphere_volume
    radius = 3
    print("Volume of sphere:", sphere_volume(radius))
    
    # Test is_palindrome
    word = "madam"
    print("Is palindrome:", is_palindrome(word))
    
    # Test histogram
    hist_values = [4, 9, 7]
    print("Histogram:")
    histogram(hist_values)

if __name__ == "__main__":
    main()