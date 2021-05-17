# https://www.codewars.com/kata/520b9d2ad5c005041100000f/train/python

def pig_it(text):
    words = text.split(' ')
    result = []
    for word in words:
        if 'a' <= word[0] <= 'z' or 'A' <= word[0] <= 'Z':
            result.append(word[1:] + word[0] + "ay")
        else:
            result.append(word)
    return " ".join(result)
