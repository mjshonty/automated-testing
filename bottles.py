
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


