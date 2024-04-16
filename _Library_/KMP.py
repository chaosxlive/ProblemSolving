def find_all(text, pattern):
    pattern = list(pattern)
    sfts = [1] * (len(pattern) + 1)
    sft = 1
    for pos in range(len(pattern)):
        while sft <= pos and pattern[pos] != pattern[pos - sft]:
            sft += sfts[pos - sft]
        sfts[pos + 1] = sft
    start = 0
    mL = 0
    for c in text:
        while mL == len(pattern) or mL >= 0 and pattern[mL] != c:
            start += sfts[mL]
            mL -= sfts[mL]
        mL += 1
        if mL == len(pattern):
            yield start
    return mL
