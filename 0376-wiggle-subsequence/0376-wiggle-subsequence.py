class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        # Track the length of the longest wiggle subsequence 
        # ending with a positive/negative difference.
        up = 1
        down = 1
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                # Sequence went up, so look at the length of the best sequence that ended going down
                up = down + 1
            elif nums[i] < nums[i - 1]:
                # Sequence went down, so look at the length of the best sequence that ended going up
                down = up + 1
            # If nums[i] == nums[i-1], we do nothing and skip the duplicate
                
        return max(up, down)