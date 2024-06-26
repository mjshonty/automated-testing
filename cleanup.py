
# Function to cleanup language.  It replaces bad words with less bad words.

def cleanup(message):
    words = [
        ('damn', 'darn'),
        ('hell', 'hades'),
        ('shit', 'poop')
    ]
    for (word, replacement) in words:
        message = message.replace(word, replacement)
    return message

# Test cases

def test_cleanup():
    x = "damn this shit to hell"
    assert cleanup(x) == "darn this poop to hades"
    pass
