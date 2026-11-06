class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [-1] * n
        stack = []  # This will store the indices of the elements
        
        # Loop through the array twice to handle the circular condition
        for i in range(2 * n):
            idx = i % n
            # While stack is not empty and the current element is greater 
            # than the element corresponding to the index at the top of the stack
            while stack and nums[stack[-1]] < nums[idx]:
                res[stack.pop()] = nums[idx]
            
            # We only need to push indices from the first pass
            if i < n:
                stack.append(idx)
                
        return res