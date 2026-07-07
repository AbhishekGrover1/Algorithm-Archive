class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []  # Stores pairs of (index, height)
        max_area = 0
        
        for i, h in enumerate(heights):
            start = i
            # Maintain a monotonic increasing stack
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                # Calculate area with the popped height as the shortest bar
                max_area = max(max_area, height * (i - idx))
                # The popped bar's start position is where the current shorter bar can extend backwards
                start = idx
                
            stack.append((start, h))
            
        # Clear out any remaining bars left in the stack
        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))
            
        return max_area