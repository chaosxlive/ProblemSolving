# https://leetcode.com/problems/number-of-valid-words-in-a-sentence/

import re


class Solution:
    def countValidWords(self, sentence: str) -> int:
        return len(re.findall("(^| )([a-zA-Z]+(-[a-zA-Z]+)?((?=($|\ ))|[!,.](?=\ |$))|[!,.](?=\ |$))", sentence))
