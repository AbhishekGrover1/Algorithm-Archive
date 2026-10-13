class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"
        
        hex_chars = "0123456789abcdef"
        result = ""
        
        # Handle two's complement for negative numbers (32-bit integer)
        if num < 0:
            num += 2**32
            
        while num > 0:
            digit = num % 16
            result = hex_chars[digit] + result
            num //= 16
            
        return result