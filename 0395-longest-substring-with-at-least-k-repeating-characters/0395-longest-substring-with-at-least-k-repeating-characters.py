class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # Base case: if the string is shorter than k, it's impossible to have k repeating characters.
        if len(s) < k:
            return 0
            
        # Check every unique character in the current string
        for c in set(s):
            if s.count(c) < k:
                # If a character appears less than k times, it cannot be part of the valid substring.
                # Split the string by this character and recursively check the resulting substrings.
                return max(self.longestSubstring(sub, k) for sub in s.split(c))
                
        # If all characters in the string appear at least k times, the whole string is valid.
        return len(s)