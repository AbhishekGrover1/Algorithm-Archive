class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Base cases
        if n <= 2:
            return n
        
        # first represents ways(i-2), second represents ways(i-1)
        first, second = 1, 2
        
        # Iteratively calculate ways up to n
        for i in range(3, n + 1):
            current = first + second
            first = second
            second = current
            
        return second