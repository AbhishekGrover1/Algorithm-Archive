class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        R, C = len(board), len(board[0])
        
        # Pruning 1: If the word is longer than the total number of cells
        if len(word) > R * C:
            return False
        
        # Pruning 2: Check character frequencies
        board_counts = {}
        for r in range(R):
            for c in range(C):
                char = board[r][c]
                board_counts[char] = board_counts.get(char, 0) + 1
                
        word_counts = {}
        for char in word:
            word_counts[char] = word_counts.get(char, 0) + 1
            
        for char, count in word_counts.items():
            if board_counts.get(char, 0) < count:
                return False
                
        # Pruning 3: Optimize start direction (branching factor reduction)
        # If the first letter occurs more frequently than the last letter,
        # reversing the word minimizes our DFS search paths.
        if board_counts[word[0]] > board_counts[word[-1]]:
            word = word[::-1]

        def dfs(r, c, index):
            # Base case: Found all characters
            if index == len(word):
                return True
                
            # Boundary and mismatch checks
            if r < 0 or r >= R or c < 0 or c >= C or board[r][c] != word[index]:
                return False
            
            # Track visited by temporarily modifying the board
            temp = board[r][c]
            board[r][c] = "#"
            
            # Explore 4 directions
            found = (dfs(r + 1, c, index + 1) or
                     dfs(r - 1, c, index + 1) or
                     dfs(r, c + 1, index + 1) or
                     dfs(r, c - 1, index + 1))
            
            # Backtrack
            board[r][c] = temp
            return found

        # Try starting DFS from every cell matching the first character
        for r in range(R):
            for c in range(C):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True
                        
        return False