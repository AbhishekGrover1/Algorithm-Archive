class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.count = 0
        
        # Tracking sets for columns and diagonals
        cols = set()
        pos_diag = set()  # (r + c) remains constant
        neg_diag = set()  # (r - c) remains constant
        
        def backtrack(r):
            if r == n:
                self.count += 1
                return
            
            for c in range(n):
                # If the column or either diagonal is under attack, skip
                if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
                    continue
                
                # Place the queen (Choose)
                cols.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)
                
                # Move to the next row (Explore)
                backtrack(r + 1)
                
                # Remove the queen (Unchoose)
                cols.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)
                
        backtrack(0)
        return self.count