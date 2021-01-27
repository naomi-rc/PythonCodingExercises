import string, re

PUNCTUATION = string.punctuation.replace("'", "")
APOSTROPHE = "'"
DELIMETER = " "

def count_words(sentence):
    result = {}
    sentence = replace_punctuation(sentence)
    sentence = sentence.lower()
    words_within_apostrophes = re.findall(r"([\"\']\w+[\"\'])", sentence) #trying to replace instances of words wrapped in quotes with the actual word
    
    for word in words_within_apostrophes:
        replacement =  word.replace("'", "")
        replacement = replacement.replace('"', "")
        sentence = sentence.replace(word, replacement)

    words = sentence.split(DELIMETER)
    
    for word in words:
        if word not in string.whitespace:
            #print
            if word.count(APOSTROPHE) > 1:
                #print(word)
                word = word.replace(APOSTROPHE, "")
                
            #print(word)
            #print(r"\b"+ word +r"\b")
            
            result.update({str(word) : len(re.findall(r"\b"+ word +r"\b", sentence))})   

    return result


def replace_punctuation(sentence):
    for symbol in PUNCTUATION + string.whitespace:
        sentence = sentence.replace(symbol, DELIMETER)
    return sentence
     




def count_words2(sentence):
    result = {}
    for symbol in PUNCTUATION + string.whitespace:
        sentence = sentence.replace(symbol, DELIMETER)
    word_set = sentence.split(DELIMETER)
    print(word_set)
    for word in word_set:
        if word:
            result.update({word : word_set.count(word) })
    return result

#print(count_words("''hey''"))
print(count_words("car: carpet as java: javascript!!&@$%^&"))

#print(str("''hey''").replace("'", ""))
#print("''hey''".replace("'", ""))
#print(string.punctuation)