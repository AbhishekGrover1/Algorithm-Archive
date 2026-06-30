class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        # Initialize stack with -1 to serve as a base for length calculation
        stack = [-1]
        
        for i, char in enumerate(s):
            if char == '(':
                # Push the index of '('
                stack.append(i)
            else:
                # Pop the last opening parenthesis or base index
                stack.pop()
                
                if not stack:
                    # If stack is empty, this ')' is unmatched; it becomes the new base
                    stack.append(i)
                else:
                    # Calculate the length of the current valid substring
                    max_len = max(max_len, i - stack[-1])
                    
        return max_len