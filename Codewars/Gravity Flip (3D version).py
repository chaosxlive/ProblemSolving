# https://www.codewars.com/kata/5f849ab530b05d00145b9495/train/python

def flip(d, a):
    if d == 'L':
        return [sorted(row, reverse=True) for row in a]
    elif d == 'R':
        return [sorted(row) for row in a]
    else:
        temp = [[row[col] for row in a] for col in range(len(a[0]))]
        for row in temp:
            row.sort(reverse=(d == 'U'))
        return [[row[col] for row in temp] for col in range(len(temp[0]))]
