
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

