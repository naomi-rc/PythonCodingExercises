
def is_isogram(string):
    string = string.lower()
    return 0 == sum(1 for i, char in enumerate(string) if str(char).isalpha() and string[i:].count(char) > 1)
