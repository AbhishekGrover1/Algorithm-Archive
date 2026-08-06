class Solution(object):

    def isPowerOfFour(self, n):
        """

        :type n: int

        :rtype: bool

        """
        # 1. n > 0: Must be positive
        # 2. (n & (n - 1)) == 0: Checks if n is a power of 2 (has exactly one '1' bit)
        # 3. (n & 0x55555555) != 0: Ensures the set bit is at an even position (0, 2, 4, ...)
        return n > 0 and (n & (n - 1)) == 0 and (n & 0x55555555) != 0