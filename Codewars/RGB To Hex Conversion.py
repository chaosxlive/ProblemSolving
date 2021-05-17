# https://www.codewars.com/kata/513e08acc600c94f01000001/train/python

def rgb(r, g, b):
    if r < 0:
        r = 0
    elif r > 255:
        r = 255
    if g < 0:
        g = 0
    elif g > 255:
        g = 255
    if b < 0:
        b = 0
    elif b > 255:
        b = 255
    convertIntToHex = {0: "0",
                       1: "1", 2: "2", 3: "3", 4: "4", 5: "5",
                       6: "6", 7: "7", 8: "8", 9: "9", 10: "A",
                       11: "B", 12: "C", 13: "D", 14: "E", 15: "F"
                       }
    return convertIntToHex[r // 16] + convertIntToHex[r % 16] + convertIntToHex[g // 16] + convertIntToHex[g % 16] + convertIntToHex[b // 16] + convertIntToHex[b % 16]
