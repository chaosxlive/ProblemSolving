# https://leetcode.com/problems/unique-morse-code-words/

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = {
            'a': ".-", 'b': "-...", 'c': "-.-.", 'd': "-..", 'e': ".",
            'f': "..-.", 'g': "--.", 'h': "....", 'i': "..", 'j': ".---",
            'k': "-.-", 'l': ".-..", 'm': "--", 'n': "-.", 'o': "---",
            'p': ".--.", 'q': "--.-", 'r': ".-.", 's': "...", 't': "-",
            'u': "..-", 'v': "...-", 'w': ".--", 'x': "-..-", 'y': "-.--",
            'z': "--.."
        }

        appearence = set()

        for word in words:
            code = ""
            for c in word:
                code += morse[c]
            appearence.add(code)
        
        return len(appearence)
