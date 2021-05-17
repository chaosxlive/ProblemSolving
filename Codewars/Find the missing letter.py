# https://www.codewars.com/kata/5839edaa6754d6fec10000a2/train/python

def find_missing_letter(chars):
    for index in range(len(chars) - 1):
        if ord(chars[index]) + 1 != ord(chars[index + 1]):
            return chr(ord(chars[index]) + 1)
    return chr(ord(chars[-1]) + 1)