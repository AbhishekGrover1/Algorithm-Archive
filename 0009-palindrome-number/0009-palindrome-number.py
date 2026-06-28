class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Special cases:
        # 1. Negative numbers are not palindromes (e.g., -121 end with '-')
        # 2. Numbers ending in 0 are not plaindromes except for 0 itself (e.g., 10 , 200)
        if x < 0 or (x % 10 == 0 and x !=0):
            return False 

        reversed_half = 0
        # Reversed the second half of the number 
        while x > reversed_half:
            reversed_half = (reversed_half * 10) + (x % 10)
            x //= 10

        # if the number has not an odd length, we can get rid of the middle digit 
        # by doing reversed_half // 10 (e.g., for 121, x = 1, reversed_half = 12)
        return x == reversed_half or x == reversed_half // 10