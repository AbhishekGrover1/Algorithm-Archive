class Solution(object):
    def licenseKeyFormatting(self, s, k):
        # Step 1: Remove dashes and convert to uppercase
        s = s.replace("-", "").upper()
        
        if not s:
            return ""
            
        n = len(s)
        
        # Step 2 & 3: Find the length of the first group
        first_group_len = n % k if n % k != 0 else k
        
        # Initialize result list with the first group
        res = [s[:first_group_len]]
        
        # Step 4: Add remaining characters in chunks of size k
        for i in range(first_group_len, n, k):
            res.append(s[i:i+k])
            
        # Step 5: Join with dashes
        return "-".join(res)