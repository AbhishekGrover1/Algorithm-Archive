class Solution(object):
    def getMaxRepetitions(self, s1, n1, s2, n2):
        """
        :type s1: str
        :type n1: int
        :type s2: str
        :type n2: int
        :rtype: int
        """
        if n1 == 0:
            return 0
            
        s1_count = 0 # Count of s1 processed
        s2_count = 0 # Count of full s2 matched
        p2 = 0       # Pointer for s2
        
        # Dictionary to store the state: 
        # p2 -> (s1_count, s2_count)
        recall = {}
        
        while s1_count < n1:
            # Match characters of s1 with s2
            for c in s1:
                if c == s2[p2]:
                    p2 += 1
                    if p2 == len(s2):
                        s2_count += 1
                        p2 = 0
            
            s1_count += 1
            
            # Check if we have seen this p2 at the start of an s1 block before
            if p2 in recall:
                prev_s1_count, prev_s2_count = recall[p2]
                
                # Length of the cycle in terms of s1 blocks and s2 matches
                cycle_s1_length = s1_count - prev_s1_count
                cycle_s2_length = s2_count - prev_s2_count
                
                # Fast forward the remaining s1 blocks using the detected cycle
                remaining_s1 = n1 - s1_count
                num_cycles = remaining_s1 // cycle_s1_length
                
                s1_count += num_cycles * cycle_s1_length
                s2_count += num_cycles * cycle_s2_length
            else:
                # Record the state for cycle detection
                recall[p2] = (s1_count, s2_count)
                
        # We need str2 which is s2 concatenated n2 times
        return s2_count // n2