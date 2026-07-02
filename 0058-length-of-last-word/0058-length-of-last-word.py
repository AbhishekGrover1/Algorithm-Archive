class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = 0
        i = len(s) - 1
        
        # 1. Skip any trailing spaces at the end of the string
        while i >= 0 and s[i] == ' ':
            i -= 1
            
        # 2. Count characters until we hit another space or the start of the string
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1
            
        return length