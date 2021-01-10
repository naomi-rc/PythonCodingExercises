
def is_isogram(string):
    return len(list(filter(str.isalpha, string.lower()))) == len(set(filter(str.isalpha, string.lower())))

