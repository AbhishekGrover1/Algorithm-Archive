import math

class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        # Start from the square root of the area and go downwards
        w = int(math.sqrt(area))
        
        # Find the first width that perfectly divides the area
        while area % w != 0:
            w -= 1
            
        # The length will be area // w
        return [area // w, w]