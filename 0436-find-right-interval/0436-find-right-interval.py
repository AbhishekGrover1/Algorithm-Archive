import bisect

class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        # Create a sorted list of tuples: (start_time, original_index)
        starts = sorted([(interval[0], i) for i, interval in enumerate(intervals)])
        
        # Extract just the start times to make binary search simpler
        start_times = [s[0] for s in starts]
        
        res = []
        for interval in intervals:
            end = interval[1]
            
            # Find the leftmost index where 'end' can be inserted
            idx = bisect.bisect_left(start_times, end)
            
            if idx < len(starts):
                # We found a start time >= end, append the original index
                res.append(starts[idx][1])
            else:
                # No start time is >= end
                res.append(-1)
                
        return res