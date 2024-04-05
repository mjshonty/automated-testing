
# Main code that counts letters in a string

def count_letters(input_string):
    letters = {}
    for letter in input_string:
        letters.setdefault(letter, 0)
        letters[letter] += 1
    return letters
        

# Code to test the count_letters function
