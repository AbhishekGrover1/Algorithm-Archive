class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unique_nums = sorted(list(set(nums)), reverse=True)
        
        # If there are 3 or more distinct elements, return the 3rd one
        if len(unique_nums) >= 3:
            return unique_nums[2]
        
        # Otherwise, return the maximum element
        return unique_nums[0]