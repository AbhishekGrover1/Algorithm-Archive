class Solution(object):
    def readBinaryWatch(self, turnedOn):
        """
        :type turnedOn: int
        :rtype: List[str]
        """
        res = []
        # Iterate over all possible hours (0 to 11) and minutes (0 to 59)
        for h in range(12):
            for m in range(60):
                # Count total set bits (1s in binary) for both hour and minute
                if bin(h).count('1') + bin(m).count('1') == turnedOn:
                    res.append("{}:{:02d}".format(h, m))
        return res