class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # Pointer to keep track of where the next non-zero element should go
        last_non_zero_found_at = 0
        
        # Iterate through the array
        for i in range(len(nums)):
            if nums[i] != 0:
                # Swap current non-zero element with the element at the last_non_zero_found_at index
                nums[last_non_zero_found_at], nums[i] = nums[i], nums[last_non_zero_found_at]
                last_non_zero_found_at += 1