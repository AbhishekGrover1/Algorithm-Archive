class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :type rtype: List[List[int]]
        """
        result = []
        
        def backtrack(i, current_combo, current_sum):
            # Base Case: If we hit the target exactly, record the valid combination
            if current_sum == target:
                result.append(list(current_combo))
                return
            
            # Base Case: If the sum exceeds the target or we run out of candidates
            if current_sum > target or i >= len(candidates):
                return
            
            # Choice 1: Include candidates[i]. (We don't increment 'i' because we can reuse it)
            current_combo.append(candidates[i])
            backtrack(i, current_combo, current_sum + candidates[i])
            
            # Backtrack: Remove the last added element before exploring the next choice
            current_combo.pop()
            
            # Choice 2: Skip candidates[i] and move to the next candidate element
            backtrack(i + 1, current_combo, current_sum)
            
        backtrack(0, [], 0)
        return result
        