class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        max_len = 0
        # Dictionary to store the length of the path down to a specific depth
        path_len = {0: 0}
        
        for line in input.split('\n'):
            # Count tabs to determine the depth of the current file/directory
            name = line.lstrip('\t')
            depth = len(line) - len(name)
            
            if '.' in name:
                # If it's a file, update the max length found so far
                max_len = max(max_len, path_len[depth] + len(name))
            else:
                # If it's a directory, calculate the length for its sub-items
                # +1 is for the '/' that will be appended
                path_len[depth + 1] = path_len[depth] + len(name) + 1
                
        return max_len