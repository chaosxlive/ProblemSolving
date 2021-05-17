# https://www.codewars.com/kata/54b72c16cd7f5154e9000457/train/python

import re


def decode_bits(bits):
    # ToDo: Accept 0's and 1's, return dots, dashes and spaces
    bits = bits.strip('0')
    if '0' not in bits:
        return '.'
    unitTime = min(min(map(lambda x: len(x), re.split('0+', bits))), min(map(lambda x: len(x), re.split('1+', bits)[1:-1])))
    return re.sub(
        '0{' + str(unitTime) + '}',
        '',
        re.sub(
            '0{' + str(unitTime * 3) + '}',
            ' ',
            re.sub(  # Space between word
                '0{' + str(unitTime * 7) + '}',
                '   ',
                re.sub(  # Dot
                    '1{' + str(unitTime) + '}',
                    '.',
                    re.sub(  # Dash
                        '1{' + str(unitTime * 3) + '}',
                        '-',
                        bits
                    )
                )
            )
        )
    )


def decode_morse(morseCode):
    # ToDo: Accept dots, dashes and spaces, return human-readable message
    splitted = morseCode.strip(' ').split(' ')
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
