class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        # Split the path by '/' to process each directory component
        components = path.split('/')
        stack = []
        
        for component in components:
            # If it's empty (caused by '//') or a single dot '.', do nothing
            if not component or component == '.':
                continue
            
            # If it's a double dot '..', pop from stack to go up a level (if possible)
            elif component == '..':
                if stack:
                    stack.pop()
            
            # Otherwise, it's a valid directory or file name (e.g., 'home', '...', 'a')
            else:
                stack.append(component)
                
        # Join all valid directories in the stack with a single leading slash
        return '/' + '/'.join(stack)