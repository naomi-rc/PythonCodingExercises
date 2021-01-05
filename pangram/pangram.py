def is_pangram(sentence):
    ASCII_a = 97
    ASCII_z = 123
    for code in range(ASCII_a, ASCII_z):
        if chr(code) not in sentence.lower():
            return False
    return True