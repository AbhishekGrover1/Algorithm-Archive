class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []
            
        # 1. Sort intervals by their starting values
        intervals.sort(key=lambda x: x[0])
        
        merged = [intervals[0]]
        
        for i in range(1, len(intervals)):
            current = intervals[i]
            last_merged = merged[-1]
            
            # 2. If the current interval overlaps with the last merged interval,
            # merge them by updating the end time of the last merged interval.
            if current[0] <= last_merged[1]:
                last_merged[1] = max(last_merged[1], current[1])
            else:
                # 3. Otherwise, there is no overlap, so just add it to our list.
                merged.append(current)
                
        return merged