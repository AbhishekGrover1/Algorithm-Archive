from collections import defaultdict

class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        count_map = defaultdict(int)
        
        # Step 1: Store all possible sums of nums1 and nums2 in a hash map
        for a in nums1:
            for b in nums2:
                count_map[a + b] += 1
                
        count = 0
        
        # Step 2: Iterate through nums3 and nums4, checking if -(c + d) exists in the map
        for c in nums3:
            for d in nums4:
                target = -(c + d)
                if target in count_map:
                    count += count_map[target]
                    
        return count