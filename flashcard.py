
# Main code that prints out a flashcard and asks for input

def hobbit_flashcard():
    print("What has roots nobody sees, Is taller than trees, Up, up it goes, And yet never grows?")
    ans = input("Answer? ")
    ans = ans.lower()
    if (ans == "mountain"):
        return "Correct"
    else:
        return "Incorrect"

        
# Code to test the flashcard function
def test_correct(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: "mountain")
    correct = hobbit_flashcard()
    assert correct == "Correct"
    pass

def test_correct(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: "a ring")
    incorrect = hobbit_flashcard()
    assert incorrect == "Incorrect"
    pass


