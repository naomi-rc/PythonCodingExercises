import string, re

PUNCTUATION = string.punctuation.replace("'", "")
APOSTROPHE = "'"
DELIMETER = " "

def count_words(sentence):
    result = {}
    sentence = replace_punctuation(sentence)
    sentence = sentence.lower()
    words_within_apostrophes = re.findall(r"([\"\']\w+[\"\'])", sentence) 
    
    for word in words_within_apostrophes:
        replacement =  word.replace("'", "")
        replacement = replacement.replace('"', "")
        sentence = sentence.replace(word, replacement)

    words = sentence.split(DELIMETER)
    
    for word in words:
        if word not in string.whitespace:
            if word.count(APOSTROPHE) > 1:
                word = word.replace(APOSTROPHE, "")
                            
            result.update({str(word) : len(re.findall(r"\b"+ word +r"\b", sentence))})   

    return result


def replace_punctuation(sentence):
    for symbol in PUNCTUATION + string.whitespace:
        sentence = sentence.replace(symbol, DELIMETER)
    return sentence
     


