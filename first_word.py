
# Function that grabs the first word from a sentence

def first_word(sentence):
    words = sentence.split()
    return words[0]


# Code to test

def test_first_word():
    x = "this is a test"
    assert first_word(x) == "this"
    pass
