class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        
        # Helper function to get the next index after jumping
        def get_next(i):
            return (i + nums[i]) % n
            
        for i in range(n):
            if nums[i] == 0:
                continue
                
            slow = i
            fast = get_next(i)
            # Determine the direction of the current sequence
            is_forward = nums[i] > 0
            
            # Ensure we only move if the direction remains the same and we haven't visited a 0
            while (nums[fast] != 0 and (nums[fast] > 0) == is_forward and 
                   nums[get_next(fast)] != 0 and (nums[get_next(fast)] > 0) == is_forward):
                
                if slow == fast:
                    # Check if the cycle length is greater than 1
                    if slow == get_next(slow):
                        break
                    return True
                    
                slow = get_next(slow)
                fast = get_next(get_next(fast))
                
            # If no cycle was found for this path, mark all visited nodes in this path as 0 
            # so we don't process them again (O(1) space optimization)
            slow = i
            while nums[slow] != 0 and (nums[slow] > 0) == is_forward:
                nxt = get_next(slow)
                nums[slow] = 0
                slow = nxt
                
        return False