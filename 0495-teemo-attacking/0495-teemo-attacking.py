class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if not timeSeries:
            return 0
            
        total_time = 0
        for i in range(len(timeSeries) - 1):
            # Add either the full duration or the time until the next attack, whichever is smaller
            total_time += min(duration, timeSeries[i + 1] - timeSeries[i])
            
        # Add the full duration for the very last attack
        total_time += duration
        
        return total_time