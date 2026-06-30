class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n = len(haystack)
        m = len(needle)

        # If needle is longer than haystack, it can't be a substring
        if m > n:
            return -1

        # Slide the window of size m across haystack
        for i in range(n - m + 1):
            # Check if the substring matches the needle 
            if haystack[i : i + m] == needle:
                return i

        return -1