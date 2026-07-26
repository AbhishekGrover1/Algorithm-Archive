class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        seen = {}
        
        for i, num in enumerate(nums):
            # If the number exists in our map and the index difference is <= k
            if num in seen and i - seen[num] <= k:
                return True
            # Update/store the latest index for the number
            seen[num] = i
            
        return False