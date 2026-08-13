class Solution(object):

  def numSquares(self, n):

    """

    :type n: int

    :rtype: int

    """

    # dp[i] stores the least number of perfect square numbers that sum to i

    dp = [float('inf')] * (n + 1)

    dp[0] = 0



    for i in range(1, n + 1):

      j = 1

      while j * j <= i:

        dp[i] = min(dp[i], dp[i - j * j] + 1)

        j += 1



    return dp[n]