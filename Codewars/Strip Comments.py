# https://www.codewars.com/kata/51c8e37cee245da6b40000bd/train/python

def solution(string, markers):
    lines = string.split('\n')
    for index in range(len(lines)):
        for marker in markers:
            lines[index] = lines[index].split(marker)[0].strip(' ')
    return "\n".join(lines)
