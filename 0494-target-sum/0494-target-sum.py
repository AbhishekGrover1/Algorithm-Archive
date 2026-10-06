class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        total_sum = sum(nums)
        
        # If the target is entirely out of reach or if (target + total_sum) is odd, 
        # it's impossible to partition the array into valid subsets.
        if abs(target) > total_sum or (total_sum + target) % 2 != 0:
            return 0
            
        subset_target = (total_sum + target) // 2
        
        # dp[i] will store the number of ways to pick a subset that sums to i
        dp = [0] * (subset_target + 1)
        
        # There is 1 way to achieve a sum of 0 (by picking zero elements)
        dp[0] = 1 
        
        for num in nums:
            # Traverse backwards to prevent using the same element multiple times
            for i in range(subset_target, num - 1, -1):
                dp[i] += dp[i - num]
                
        return dp[subset_target]