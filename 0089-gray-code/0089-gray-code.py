class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # There are 2^n numbers in an n-bit Gray Code sequence
        num_elements = 1 << n
        result = []
        
        for i in range(num_elements):
            # Formula to convert binary code to Gray code
            result.append(i ^ (i >> 1))
            
        return result