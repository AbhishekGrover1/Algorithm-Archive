class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :type rtype: List[int]
        """
        # Dictionary to store: {value: index}
        prevMap = {}
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            # Store the current number and its index in the map
            prevMap[n] = i
            
        return # Fallback return if no solution is found (though the problem guarantees one)