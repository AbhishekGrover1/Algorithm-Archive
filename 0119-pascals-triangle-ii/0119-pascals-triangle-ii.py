class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        # Initialize the row with 1, sized to hold the entire row
        row = [1] * (rowIndex + 1)
        
        # Iteratively build each row up to rowIndex
        for i in range(1, rowIndex + 1):
            # Update from right to left to avoid using elements from the wrong iteration
            for j in range(i - 1, 0, -1):
                row[j] += row[j - 1]
                
        return row