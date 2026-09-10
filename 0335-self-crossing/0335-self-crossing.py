class Solution(object):
    def isSelfCrossing(self, distance):
        """
        :type distance: List[int]
        :rtype: bool
        """
        n = len(distance)
        if n <= 3:
            return False
            
        for i in range(3, n):
            # Case 1: Line i crosses line i - 3
            if distance[i] >= distance[i-2] and distance[i-1] <= distance[i-3]:
                return True
                
            # Case 2: Line i crosses line i - 4
            if i >= 4 and distance[i-1] == distance[i-3] and distance[i] + distance[i-4] >= distance[i-2]:
                return True
                
            # Case 3: Line i crosses line i - 5
            if i >= 5 and distance[i-2] >= distance[i-4] and distance[i-1] <= distance[i-3] and \
               distance[i-1] + distance[i-5] >= distance[i-3] and \
               distance[i] + distance[i-4] >= distance[i-2]:
                return True
                
        return False