# https://leetcode.com/problems/encode-and-decode-strings/

class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        return "".join([("0000" + str(len(s)))[-4:] + s for s in strs])

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        idx = 0
        result = []
        while idx < len(s):
            l = int(s[idx:idx + 4])
            idx += 4
            result.append(s[idx:idx + l])
            idx += l
        return result


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
