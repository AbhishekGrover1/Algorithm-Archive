class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.n = len(nums)
        self.nums = nums
        self.bit = [0] * (self.n + 1)
        
        # Build the Binary Indexed Tree
        for i in range(self.n):
            self._add(i, nums[i])

    def _add(self, index, val):
        """
        Internal method to add a value to the BIT
        """
        index += 1  # BIT is 1-indexed
        while index <= self.n:
            self.bit[index] += val
            index += index & (-index)

    def update(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        diff = val - self.nums[index]
        self.nums[index] = val
        self._add(index, diff)

    def _query(self, index):
        """
        Internal method to get the prefix sum from 0 to index
        """
        res = 0
        index += 1  # BIT is 1-indexed
        while index > 0:
            res += self.bit[index]
            index -= index & (-index)
        return res

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self._query(right) - self._query(left - 1)