def fastPow(base, power, mod=1):
    result = 1
    while power > 0:
        if power & 1 != 0:
            result = (result * base) % mod
        base = (base * base) % mod
        power >>= 1
    return result