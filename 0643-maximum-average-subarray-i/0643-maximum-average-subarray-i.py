class Solution(object):
    def findMaxAverage(self, nums, k):
        # Find the sum of the first window
        current_sum = max_sum = sum(nums[:k])
        
        # Slide the window across the rest of the array
        for i in range(k, len(nums)):
            current_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, current_sum)
            
        return max_sum / float(k)