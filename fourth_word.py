def fourth_word(sentence,word):
    words = sentence.split()
    return words[word]


def test_first_word():
    sentence = "This is a sentence"
    word = fourth_word(sentence,0)
    assert word == "This"
    pass

def test_wrong():
    sentence = "Casper the friendly ghost."
    word = fourth_word(sentence, 3)
    assert word != "friendly"
    pass

def test_number():
    sentence = "2"
    word = fourth_word(sentence,0)
    assert word != 2
    pass
