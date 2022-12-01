# https://leetcode.com/problems/web-crawler/

import queue

# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
# class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """


class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:

        def getDomain(url):
            return url.split('/')[2]

        startDomain = getDomain(startUrl)
        result = set()
        result.add(startUrl)
        visited = set()
        visited.add(startUrl)
        q = queue.Queue()
        q.put(startUrl)

        while not q.empty():
            url = q.get()
            links = htmlParser.getUrls(url)
            for link in links:
                if link in visited:
                    continue
                if getDomain(link) == startDomain:
                    result.add(link)
                    q.put(link)
                visited.add(link)
        return list(result)
