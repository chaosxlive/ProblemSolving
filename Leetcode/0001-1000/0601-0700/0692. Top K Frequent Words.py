# https://leetcode.com/problems/top-k-frequent-words/

from collections import Counter
import heapq


class Solution:

    class CmpObj:
        def __init__(self, freq, word):
            self.freq = freq
            self.word = word

        def __lt__(self, other):
            if(self.freq != other.freq):
                return self.freq < other.freq
            return self.word > other.word

        def __eq__(self, other):
            return self.freq == other.freq and self.word == other.word

    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freqs = list(map(lambda x: self.CmpObj(x[1], x[0]), Counter(words).items()))
        heapq.heapify(freqs)
        return map(lambda x: x.word, heapq.nlargest(k, freqs))
