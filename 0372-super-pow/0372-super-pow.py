class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        MOD = 1337
        
        # Base case: empty array means exponent is 0 -> a^0 = 1
        if not b:
            return 1
        
        # Pop the last digit
        last_digit = b.pop()
        
        # Calculate (a^(b without last digit))^10 % MOD
        part1 = pow(self.superPow(a, b), 10, MOD)
        
        # Calculate a^(last_digit) % MOD
        part2 = pow(a, last_digit, MOD)
        
        # Combine both parts
        return (part1 * part2) % MOD