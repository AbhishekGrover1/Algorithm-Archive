class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        # Helper function to calculate the squared distance between two points
        def dist(a, b):
            return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
        
        # Calculate distances between all 6 possible pairs of the 4 points
        distances = [
            dist(p1, p2), dist(p1, p3), dist(p1, p4),
            dist(p2, p3), dist(p2, p4), dist(p3, p4)
        ]
        
        # Convert to a set to find unique distances
        unique_distances = set(distances)
        
        # A valid square must have exactly 2 unique distances (sides and diagonals)
        # and none of those distances can be 0 (points cannot overlap).
        return len(unique_distances) == 2 and 0 not in unique_distances