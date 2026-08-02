class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Non-positive integers are not ugly numbers
        if n <= 0:
            return False
        
        # Divide out all factors of 2, 3, and 5
        for p in [2, 3, 5]:
            while n % p == 0:
                n //= p
                
        # If the remaining number is 1, it's an ugly number
        return n == 1