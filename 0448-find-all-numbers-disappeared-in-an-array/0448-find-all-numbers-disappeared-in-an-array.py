class Solution(object):
    def findDisappearedNumbers(self, nums):
        # Step 1: Mark the presence of numbers by negating values at corresponding indices
        for i in range(len(nums)):
            # Find the corresponding index for the current number
            index = abs(nums[i]) - 1
            
            # Mark as seen by making the value at that index negative
            if nums[index] > 0:
                nums[index] = -nums[index]
                
        # Step 2: Collect all indices that still contain positive numbers
        missing_numbers = []
        for i in range(len(nums)):
            if nums[i] > 0:
                # The missing number is index + 1
                missing_numbers.append(i + 1)
                
        return missing_numbers