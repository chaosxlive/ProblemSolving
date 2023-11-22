# https://leetcode.com/problems/most-common-word/

import re
from collections import Counter


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        return Counter(list(filter(lambda x: x not in set(banned + ['']), re.split('!|\?|\'|,|;|\.| ', paragraph.lower())))).most_common()[0][0]
        
