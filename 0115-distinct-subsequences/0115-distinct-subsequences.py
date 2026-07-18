class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :type rtype: int
        """
        m, n = len(s), len(t)
        
        # dp[j] stores the number of distinct subsequences matching t[0...j-1]
        dp = [0] * (n + 1)
        dp[0] = 1  # Base case: empty t can always be formed in 1 way
        
        for i in range(1, m + 1):
            # Traverse backwards to use the values from the previous row
            for j in range(n, 0, -1):
                if s[i-1] == t[j-1]:
                    dp[j] = dp[j] + dp[j-1]
                    
        return dp[n]