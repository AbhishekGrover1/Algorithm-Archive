class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        low = 0
        mid = 0
        high = len(nums) - 1
        
        while mid <= high:
            if nums[mid] == 0:
                # Swap elements at low and mid, then move both pointers forward
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                # Element is in the correct middle position, just move mid forward
                mid += 1
            else: # nums[mid] == 2
                # Swap elements at mid and high, then move high backward
                # Do not increment mid yet, as the new element at mid needs to be evaluated
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1