class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
            
        m, n = len(grid), len(grid[0])
        
        # Initialize a 1D DP array with infinity
        dp = [float('inf')] * n
        dp[0] = 0 # Base case: starting point before adding grid[0][0]
        
        for r in range(m):
            for c in range(n):
                if c == 0:
                    # For the first column, we can only come from the row above
                    dp[c] += grid[r][c]
                else:
                    # Minimum of coming from top (dp[c]) or left (dp[c-1])
                    dp[c] = grid[r][c] + min(dp[c], dp[c - 1])
                    
        return dp[-1]