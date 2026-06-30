class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        
        def backtrack(current_str, open_count, close_count):
            # Base case: if the string reaches the maximum required length
            if len(current_str) == 2 * n:
                result.append(current_str)
                return
            
            # If we can still add an opening parenthesis
            if open_count < n:
                backtrack(current_str + "(", open_count + 1, close_count)
                
            # If we can add a closing parenthesis to match an open one
            if close_count < open_count:
                backtrack(current_str + ")", open_count, close_count + 1)
                
        # Start the recursion with an empty string and 0 counts
        backtrack("", 0, 0)
        return result