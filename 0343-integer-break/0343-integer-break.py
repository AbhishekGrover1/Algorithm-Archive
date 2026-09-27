class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Base cases for n = 2 and n = 3
        if n == 2:
            return 1
        if n == 3:
            return 2
        
        # Calculate how many 3s we can use
        quotient = n // 3
        remainder = n % 3
        
        # If no remainder, just multiply all 3s
        if remainder == 0:
            return 3 ** quotient
            
        # If the remainder is 1, take one 3 out and multiply by 4
        elif remainder == 1:
            return (3 ** (quotient - 1)) * 4
            
        # If the remainder is 2, just multiply the 3s by 2
        else:
            return (3 ** quotient) * 2