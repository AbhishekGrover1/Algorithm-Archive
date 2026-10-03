class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        corners = set()
        area = 0
        min_x, min_y = float('inf'), float('inf')
        max_x, max_y = float('-inf'), float('-inf')

        for x1, y1, x2, y2 in rectangles:
            # Update the global bounding box
            min_x = min(min_x, x1)
            min_y = min(min_y, y1)
            max_x = max(max_x, x2)
            max_y = max(max_y, y2)

            # Sum the area of the current small rectangle
            area += (x2 - x1) * (y2 - y1)

            # Toggle the corners in the set
            for point in [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]:
                if point in corners:
                    corners.remove(point)
                else:
                    corners.add(point)

        # 1. The total area must match the bounding box area
        expected_area = (max_x - min_x) * (max_y - min_y)
        if area != expected_area:
            return False

        # 2. Only the 4 extreme corners should be left in the set
        expected_corners = {(min_x, min_y), (min_x, max_y), (max_x, min_y), (max_x, max_y)}
        
        return corners == expected_corners