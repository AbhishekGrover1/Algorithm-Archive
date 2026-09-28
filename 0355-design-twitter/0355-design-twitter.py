from collections import defaultdict
import heapq

class Twitter(object):
    def __init__(self):
        # Time counter to keep track of the most recent tweets
        # We decrement it because Python's heapq is a min-heap, 
        # so smaller (more negative) times will pop first.
        self.time = 0
        self.tweets = defaultdict(list) # userId -> list of (time, tweetId)
        self.following = defaultdict(set) # userId -> set of followees

    def postTweet(self, userId, tweetId):
        """
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        self.time -= 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId):
        """
        :type userId: int
        :rtype: List[int]
        """
        res = []
        heap = []
        
        # User follows themselves to see their own tweets in the feed
        users_to_check = self.following[userId].copy()
        users_to_check.add(userId)
        
        # Initialize the heap with the most recent tweet from each user
        for user in users_to_check:
            if self.tweets[user]:
                # Get the last index (most recent tweet added for this user)
                index = len(self.tweets[user]) - 1
                time, t_id = self.tweets[user][index]
                # Push (time, tweetId, user, index) to track where we are in the list
                heapq.heappush(heap, (time, t_id, user, index))
                
        # Merge the lists until we get 10 tweets or run out
        while heap and len(res) < 10:
            time, t_id, user, index = heapq.heappop(heap)
            res.append(t_id)
            
            # If the user has older tweets, add the next most recent one to the heap
            if index > 0:
                index -= 1
                next_time, next_t_id = self.tweets[user][index]
                heapq.heappush(heap, (next_time, next_t_id, user, index))
                
        return res

    def follow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)