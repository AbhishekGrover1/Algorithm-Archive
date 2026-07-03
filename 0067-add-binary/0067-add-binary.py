class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = []
        carry = 0
        
        # Pointers for both strings starting at the end
        i = len(a) - 1
        j = len(b) - 1
        
        # Loop as long as there are digits to process or a carry remains
        while i >= 0 or j >= 0 or carry:
            total = carry
            
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
                
            # Append the remainder (binary digit)
            result.append(str(total % 2))
            # Calculate the new carry
            carry = total // 2
            
        # Reverse the result list and join into a string
        return "".join(result[::-1])