# https://www.codewars.com/kata/54b724efac3d5402db00065e/train/python

def decodeMorse(morse_code):
    # ToDo: Accept dots, dashes and spaces, return human-readable message
    splitted = morse_code.strip(' ').split(' ')
    index = 0
    result = []
    while index < len(splitted):
        if len(splitted[index]) == 0:
            result.append(' ')
            index += 2
            continue
        result.append(MORSE_CODE[splitted[index]])
        index += 1
    return "".join(result)
