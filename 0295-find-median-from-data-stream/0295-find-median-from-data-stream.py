import heapq

class MedianFinder(object):

    def __init__(self):
        # Max-heap to store the smaller half of numbers (inverted values for Python's min-heap)
        self.small = []
        # Min-heap to store the larger half of numbers
        self.large = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        # Step 1: Add to max-heap (small), then balance to min-heap (large)
        heapq.heappush(self.small, -num)
        heapq.heappush(self.large, -heapq.heappop(self.small))
        
        # Step 2: Maintain size property: len(small) >= len(large)
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2.0