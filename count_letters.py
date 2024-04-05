
# Main code that counts letters in a string

def count_letters(input_string):
    letters = {}
    for letter in input_string:
        letters.setdefault(letter, 0)
        letters[letter] += 1
    return letters
        

# Code to test the count_letters function
def test_count_letters():
    message1 = "HI"
    test1 = count_letters(message1)
    assert ('H',1) in test1.items()
    assert ('I',1) in test1.items()
    pass

def test_number():
    message2 = "initial"
    test2 = count_letters(message2)
    assert ('i', 3) in test2.items()
    pass

def test_empty():
    message3 = ""
    test3 = count_letters(message3)
    test3 == {}
    pass

def test_2_conditions():
    message4 = "hello to you"
    test4 = count_letters(message4)
    assert ('y', 1) in test4.items()
    assert ('l', 8) not in test4.items()
    pass