from collections import deque

class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(mat), len(mat[0])
        queue = deque()
        
        # Initialize the queue with all '0' cells and mark '1's with infinity
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    queue.append((r, c))
                else:
                    mat[r][c] = float('inf')
        
        # Directions for adjacent cells: down, up, right, left
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # Perform BFS
        while queue:
            r, c = queue.popleft()
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # If the adjacent cell is within bounds and can be reached in a shorter distance
                if 0 <= nr < m and 0 <= nc < n and mat[nr][nc] > mat[r][c] + 1:
                    mat[nr][nc] = mat[r][c] + 1
                    queue.append((nr, nc))
                    
        return mat