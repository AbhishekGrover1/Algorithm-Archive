class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        # Edge Case 1: If desiredTotal is <= 0, first player wins immediately
        if desiredTotal <= 0:
            return True
        
        # Edge Case 2: If the sum of all numbers is less than desiredTotal, no player can win
        sum_all = (maxChoosableInteger * (maxChoosableInteger + 1)) // 2
        if sum_all < desiredTotal:
            return False
        
        memo = {}

        def can_win(mask, current_total):
            if mask in memo:
                return memo[mask]
            
            for i in range(maxChoosableInteger):
                # Check if the integer (i + 1) has not been picked yet
                if not (mask & (1 << i)):
                    val = i + 1
                    # Winning condition:
                    # 1. Choosing this number reaches or exceeds desiredTotal
                    # 2. OR the next player cannot win from the remaining choices
                    if current_total + val >= desiredTotal or not can_win(mask | (1 << i), current_total + val):
                        memo[mask] = True
                        return True
            
            memo[mask] = False
            return False

        return can_win(0, 0)