class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        
        def backtrack(start, path):
            # Every distinct path we explore is a valid subset
            res.append(list(path))
            
            # Explore further elements to build larger subsets
            for i in range(start, len(nums)):
                # Include nums[i] in the current subset
                path.append(nums[i])
                # Move onto the next elements
                backtrack(i + 1, path)
                # Exclude nums[i] from the current subset (backtrack)
                path.pop()
                
        backtrack(0, [])
        return res