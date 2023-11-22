# https://leetcode.com/problems/encode-and-decode-tinyurl/

class Codec:
    def __init__(self) -> None:
        self.urls = []
        self.count = -1

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.urls.append(longUrl)
        self.count += 1
        return str(self.count)
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.urls[int(shortUrl)]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))