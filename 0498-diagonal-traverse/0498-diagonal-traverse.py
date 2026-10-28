class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        if not mat or not mat[0]:
            return []
            
        m, n = len(mat), len(mat[0])
        
        # Create an array of lists to hold elements for each diagonal
        diagonals = [[] for _ in range(m + n - 1)]
        
        # Group elements by the sum of their indices (r + c)
        for r in range(m):
            for c in range(n):
                diagonals[r + c].append(mat[r][c])
                
        res = []
        
        # Assemble the final result
        for d in range(m + n - 1):
            if d % 2 == 0:
                # Even diagonal: elements go up-right, so we reverse the standard top-to-bottom order
                res.extend(diagonals[d][::-1])
            else:
                # Odd diagonal: elements go down-left, which matches the standard top-to-bottom order
                res.extend(diagonals[d])
                
        return res