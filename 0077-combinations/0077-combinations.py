class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        
        def backtrack(start, path):
            # Base case: if the combination is done
            if len(path) == k:
                res.append(list(path))
                return
            
            # Optimization: No need to iterate if there aren't enough numbers left 
            # to complete a combination of size k
            for i in range(start, n + 1):
                # Make a choice
                path.append(i)
                # Recurse with the next integer
                backtrack(i + 1, path)
                # Undo the choice (backtrack)
                path.pop()
                
        backtrack(1, [])
        return res