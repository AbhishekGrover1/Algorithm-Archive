class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
            
        result = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        
        while top <= bottom and left <= right:
            # 1. Traverse from left to right across the top row
            for c in range(left, right + 1):
                result.append(matrix[top][c])
            top += 1 # Move the top boundary down
            
            # 2. Traverse from top to bottom down the right column
            for r in range(top, bottom + 1):
                result.append(matrix[r][right])
            right -= 1 # Move the right boundary left
            
            # 3. Traverse from right to left across the bottom row
            # (Check needed if the top boundary has bypassed the bottom)
            if top <= bottom:
                for c in range(right, left - 1, -1):
                    result.append(matrix[bottom][c])
                bottom -= 1 # Move the bottom boundary up
                
            # 4. Traverse from bottom to top up the left column
            # (Check needed if the left boundary has bypassed the right)
            if left <= right:
                for r in range(bottom, top - 1, -1):
                    result.append(matrix[r][left])
                left += 1 # Move the left boundary right
                
        return result