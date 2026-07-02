class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_reachable = 0
        
        for i, jump in enumerate(nums):
            # If the current index is greater than the max reachable index, 
            # it means we cannot even reach this spot.
            if i > max_reachable:
                return False
            
            # Update the furthest index we can reach from the current spot
            max_reachable = max(max_reachable, i + jump)
            
            # Optimization: If we can already reach or pass the last index, return True
            if max_reachable >= len(nums) - 1:
                return True