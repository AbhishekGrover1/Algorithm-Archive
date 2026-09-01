class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        
        ROWS, COLS = len(board), len(board[0])
        
        # Directions for the 8 neighbors (horizontal, vertical, diagonal)
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]
        
        for r in range(ROWS):
            for c in range(COLS):
                # Count live neighbors from the current state
                live_neighbors = 0
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS:
                        # Check if the neighbor was originally alive (1 or 3)
                        if board[nr][nc] % 2 == 1:
                            live_neighbors += 1
                
                # Rule 1 & 3: Live cell with < 2 or > 3 live neighbors dies (state 1 -> stays 1)
                # Rule 2: Live cell with 2 or 3 live neighbors lives on (state 3)
                if board[r][c] == 1:
                    if live_neighbors == 2 or live_neighbors == 3:
                        board[r][c] = 3
                
                # Rule 4: Dead cell with exactly 3 live neighbors becomes live (state 2)
                else:
                    if live_neighbors == 3:
                        board[r][c] = 2
                        
        # Second pass: update the board to the final state (0 or 1)
        for r in range(ROWS):
            for c in range(COLS):
                board[r][c] >>= 1