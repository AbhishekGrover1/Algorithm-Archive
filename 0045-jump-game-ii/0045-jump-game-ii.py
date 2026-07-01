class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Edge case: If there's only 1 element, we are already at the destination
        if len(nums) <= 1:
            return 0
            
        jumps = 0
        current_jump_end = 0
        farthest = 0
        
        # Iterate up to len(nums) - 1 because we don't need to jump once we land on the last index
        for i in range(len(nums) - 1):
            # Continuously update the farthest index we can reach
            farthest = max(farthest, i + nums[i])
            
            # If we've reached the end of the current jump window
            if i == current_jump_end:
                jumps += 1
                current_jump_end = farthest
                
                # Optimization: If the current reach already gets us to the end, break early
                if current_jump_end >= len(nums) - 1:
                    break
                    
        return jumps