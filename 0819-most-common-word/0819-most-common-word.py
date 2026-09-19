class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        # Replace punctuation characters with spaces to handle edge cases like "ball,"
        for c in "!?',;.":
            paragraph = paragraph.replace(c, " ")
            
        # Convert the paragraph to lowercase and split it into a list of words
        words = paragraph.lower().split()
        
        # Convert banned list to a set for faster O(1) lookup
        banned_set = set(banned)
        
        # Count frequencies of valid (non-banned) words
        counts = {}
        for word in words:
            if word not in banned_set:
                counts[word] = counts.get(word, 0) + 1
                
        # Return the word with the highest frequency
        return max(counts, key=counts.get)