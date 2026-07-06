class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res = []
        current_line = []
        current_length = 0  # Tracks total length of characters in current_line (excluding spaces)

        for word in words:
            # current_length + len(word) + len(current_line) represents:
            # letters so far + new word letters + minimum 1 space between each word
            if current_length + len(word) + len(current_line) > maxWidth:
                # Format the completed line and add to results
                res.append(self.formatLine(current_line, current_length, maxWidth, False))
                current_line = []
                current_length = 0
            
            current_line.append(word)
            current_length += len(word)

        # Handle the last remaining line (must be left-justified)
        if current_line:
            res.append(self.formatLine(current_line, current_length, maxWidth, True))

        return res

    def formatLine(self, line, current_length, maxWidth, is_last):
        # Case 1: Last line or line contains only one word -> Left Justified
        if is_last or len(line) == 1:
            return " ".join(line).ljust(maxWidth)
        
        # Case 2: Middle line with multiple words -> Fully Justified
        total_spaces = maxWidth - current_length
        gaps = len(line) - 1
        
        base_spaces = total_spaces // gaps
        extra_spaces = total_spaces % gaps
        
        # Build the line by distributing spaces evenly
        result = []
        for i in range(gaps):
            result.append(line[i])
            # Add base spaces + 1 extra space if we are still within the remainder count
            result.append(" " * (base_spaces + (1 if i < extra_spaces else 0)))
        
        # Don't forget to append the last word of the line
        result.append(line[-1])
        
        return "".join(result)