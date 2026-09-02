class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # Initialize a DP array with the values of the last row
        dp = triangle[-1][:]
        
        # Work bottom-up starting from the second to last row
        for row in range(len(triangle) - 2, -1, -1):
            for i in range(len(triangle[row])):
                # Update the DP array with the minimum path sum to the current node
                dp[i] = triangle[row][i] + min(dp[i], dp[i + 1])
                
        return dp[0]