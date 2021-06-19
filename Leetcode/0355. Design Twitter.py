# https://leetcode.com/problems/design-twitter/

from collections import defaultdict


class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.time = 0
        self.followerDupCheck = defaultdict(set)
        self.follower = defaultdict(list)
        self.posts = defaultdict(list)  # (time, tweetId)

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.posts[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        selfIndex = len(self.posts[userId]) - 1
        followIndices = [(len(self.posts[f]) - 1) for f in self.follower[userId]]

        count = 0
        result = []
        while count < 10:
            latestIndex = -1
            latestTime = -1

            for i in range(len(self.follower[userId])):
                if followIndices[i] >= 0 and self.posts[self.follower[userId][i]][followIndices[i]][0] > latestTime:
                    latestTime = self.posts[self.follower[userId][i]][followIndices[i]][0]
                    latestIndex = i
            if selfIndex >= 0 and self.posts[userId][selfIndex][0] > latestTime:
                result.append(self.posts[userId][selfIndex][1])
                selfIndex -= 1
            else:
                if latestIndex == -1:
                    break
                result.append(self.posts[self.follower[userId][latestIndex]][followIndices[latestIndex]][1])
                followIndices[latestIndex] -= 1
            count += 1
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followeeId not in self.followerDupCheck[followerId]:
            self.follower[followerId].append(followeeId)
            self.followerDupCheck[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        try:
            self.follower[followerId].remove(followeeId)
            self.followerDupCheck[followerId].remove(followeeId)
        except:
            pass


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
