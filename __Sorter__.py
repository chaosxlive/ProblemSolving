import os
import re

LEETCODE_ROOT = './Leetcode'


for name in os.listdir(LEETCODE_ROOT):
    source = f"{LEETCODE_ROOT}/{name}"
    if os.path.isdir(source):
        continue
    mth = re.match('^(\d{4})\. ', name)
    if mth is None:
        continue
    if mth.lastindex < 1:
        continue
    print(f'Source: {source}')
    # Layer 1
    leadingNum = mth[1][:1]
    if mth[1][1:4] == '000':
        leadingNum = str(int(leadingNum) - 1).rjust(1, '0')
    dirLayer1 = f"{leadingNum}001-{str(int(leadingNum) + 1).rjust(1, '0')}000"
    # Layer 2
    leadingNum = mth[1][:2]
    if mth[1][2:4] == '00':
        leadingNum = str(int(leadingNum) - 1).rjust(2, '0')
    dirLayer2 = f"{leadingNum}01-{str(int(leadingNum) + 1).rjust(2, '0')}00"
    
    target = f"{LEETCODE_ROOT}/{dirLayer1}/{dirLayer2}/{name}"
    print(f"Target: {target}")

    os.rename(source, target)
    print('')
    