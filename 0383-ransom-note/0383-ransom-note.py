from collections import Counter

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        return all(magazine.count(char) >= ransomNote.count(char) for char in set(ransomNote))