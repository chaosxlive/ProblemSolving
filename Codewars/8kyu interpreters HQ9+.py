# https://www.codewars.com/kata/591588d49f4056e13f000001/train/python

def HQ9(code):
    if code == 'H':
        return 'Hello World!'
    elif code == 'Q':
        return 'Q'
    elif code == '9':
        result = ['99 bottles of beer on the wall, 99 bottles of beer.\n']
        for i in range(98, 1, -1):
            result.append('Take one down and pass it around, ' + str(i) + ' bottles of beer on the wall.\n' + str(i) + ' bottles of beer on the wall, ' + str(i) + ' bottles of beer.\n')
        result.append(
            'Take one down and pass it around, 1 bottle of beer on the wall.\n' +
            '1 bottle of beer on the wall, 1 bottle of beer.\n' +
            'Take one down and pass it around, no more bottles of beer on the wall.\n' +
            'No more bottles of beer on the wall, no more bottles of beer.\n' +
            'Go to the store and buy some more, 99 bottles of beer on the wall.'
        )
        return "".join(result)
    return
