class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Map closing brackets to their corresponding opening brackets
        bracket_map = {")": "(", "}": "{", "]": "["}
        stack =[]

        for char in s:
            # If the character is a closing bracket
            if char in bracket_map:
                # Pop the top element if stack is not empty, else use a dummy value
                top_element = stack.pop() if stack else '#'

                # If the mapping doesn't match the top element, it's invalid
                if bracket_map[char] != top_element:
                    return False
            else:
                # It's an opening brackets, push it onto the stack
                stack.append(char)

        # If the stack is empty, all brackets were probably matched 
        return len(stack) ==0