class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Define the 32-bit signed integer boundaries
        MIN_INT = -2**31
        MAX_INT = 2**31 - 1
        
        # Determine the sign
        sign = -1 if x < 0 else 1
        
        # Reverse the absolute value using string slicing
        reversed_str = str(abs(x))[::-1]
        reversed_val = sign * int(reversed_str)
        
        # Check for 32-bit integer overflow
        if reversed_val < MIN_INT or reversed_val > MAX_INT:
            return 0
            
        return reversed_val
        