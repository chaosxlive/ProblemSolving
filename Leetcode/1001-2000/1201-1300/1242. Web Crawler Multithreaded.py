# https://leetcode.com/problems/web-crawler/

from typing import List
import queue
from threading import Lock, Thread


# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
# class HtmlParser(object):
#     def getUrls(self, url):
#         """
#         :type url: str
#         :rtype List[str]
#         """


class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:

        def getDomain(url):
            return url.split('/')[2]

        startDomain = getDomain(startUrl)
        result = set()
        result.add(startUrl)
        visited = set()
        visited.add(startUrl)
        threadPool = queue.Queue()
        updateLock = Lock()

        def doJob(url):
            links = htmlParser.getUrls(url)
            with updateLock:
                for link in links:
                    if link in visited:
                        continue
                    if getDomain(link) == startDomain:
                        result.add(link)
                        newJob = Thread(target=doJob, args=[link])
                        threadPool.put(newJob)
                        newJob.start()
                    visited.add(link)

        firstJob = Thread(target=doJob, args=[startUrl])
        threadPool.put(firstJob)
        firstJob.start()

        while not threadPool.empty():
            with updateLock:
                job = threadPool.get()
                if job.is_alive():
                    threadPool.put(job)

        return list(result)
