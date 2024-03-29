def fastPow(base, power, mod=1):
    result = 1
    while power > 0:
        if power & 1 != 0:
            result = (result * base) % mod
        base = (base * base) % mod
        power >>= 1
    return result


def next_permutation(a):
    """
    Generate the lexicographically next permutation inplace.

    https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order

    Return false if there is no next permutation.
    """
    # Find the largest index i such that a[i] < a[i + 1]. If no such
    # index exists, the permutation is the last permutation
    for i in reversed(range(len(a) - 1)):
        if a[i] < a[i + 1]:
            break  # found
    else:  # no break: not found
        return False  # no next permutation

    # Find the largest index j greater than i such that a[i] < a[j]
    j = next(j for j in reversed(range(i + 1, len(a))) if a[i] < a[j])

    # Swap the value of a[i] with that of a[j]
    a[i], a[j] = a[j], a[i]

    # Reverse sequence from a[i + 1] up to and including the final element a[n]
    a[i + 1:] = reversed(a[i + 1:])
    return True


def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        print('\t', f)
        if n % f == 0:
            return False
        if n % (f+2) == 0:
            return False
        f += 6
    return True
