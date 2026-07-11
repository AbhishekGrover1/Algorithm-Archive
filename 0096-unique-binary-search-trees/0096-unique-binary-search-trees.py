class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        # dp[i] will store the number of unique BSTs formed by 'i' nodes
        dp = [0] * (n + 1)
        
        # Base cases
        dp[0] = 1
        dp[1] = 1
        
        # Fill the DP table
        for numberOfNodes in range(2, n + 1):
            for root in range(1, numberOfNodes + 1):
                leftSubtrees = dp[root - 1]
                rightSubtrees = dp[numberOfNodes - root]
                dp[numberOfNodes] += leftSubtrees * rightSubtrees
                
        return dp[n]