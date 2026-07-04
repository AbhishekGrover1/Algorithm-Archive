class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # Initialize a single row with 1s (representing the top row)
        row = [1] * n
        
        # Loop through the remaining rows (m - 1 times)
        for i in range(m - 1):
            # The current row will be updated in-place
            new_row = [1] * n
            # Scan from left to right, starting at index 1
            for j in range(1, n):
                # new_row[j-1] is the cell to the left
                # row[j] is the cell directly above from the previous row
                new_row[j] = new_row[j - 1] + row[j]
            row = new_row
            
        return row[-1]
        