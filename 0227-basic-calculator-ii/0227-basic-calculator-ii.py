class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        
        stack = []
        current_number = 0
        operator = '+'
        
        for i, char in enumerate(s):
            if char.isdigit():
                current_number = current_number * 10 + int(char)
            
            # If current character is an operator or it's the end of the string
            if (not char.isdigit() and char != ' ') or i == len(s) - 1:
                if operator == '+':
                    stack.append(current_number)
                elif operator == '-':
                    stack.append(-current_number)
                elif operator == '*':
                    stack.append(stack.pop() * current_number)
                elif operator == '/':
                    top = stack.pop()
                    # Truncate toward zero for division
                    stack.append(int(float(top) / current_number))
                
                operator = char
                current_number = 0
                
        return sum(stack)