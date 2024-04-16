# Prime List
PRIME_LEN = 10**3
IS_PRIME = [True] * (PRIME_LEN + 1)
PRIMES = []
IS_PRIME[0] = False
IS_PRIME[1] = False
for i in range(2, PRIME_LEN + 1):
    if IS_PRIME[i]:
        PRIMES.append(i)
    j = 0
    while i * PRIMES[j] <= PRIME_LEN:
        IS_PRIME[i * PRIMES[j]] = False
        if i % PRIMES[j] == 0:
            break
        j += 1
