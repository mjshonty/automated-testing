
# Main code that prints out a verse of the song

def bottles(n):
    print(n, "bottles of beer on the wall. ", end="")
    print(n, "bottles of beer. ", end="")
    if (n < 10):
        print("If one of those bottles should happen to fall. ", end="")
    else:
        print("Take one down, pass it around. ", end="")
    print(n-1, "bottles of beer on the wall.", end="")

        
# Code to test the bottles function
def test_verse(capsys):
    bottles(20)
    caputred = capsys.readouterr()
    assert caputred.out != """9 bottles of beer on the wall. 9 bottles of beer. If one of 
    those bottles should happen to fall. 8 bottles of beer on the wall."""
    pass

def test_verse2(capsys):
    bottles(8)
    caputred = capsys.readouterr()
    assert caputred.out != """20 bottles of beer. Take one down, pass it around. 19 bottles of beer on the wall.
    20 bottles of beer on the wall. 20 bottles of beer. Take one down, pass it around. 19 bottles of beer on the wall."""
    pass

