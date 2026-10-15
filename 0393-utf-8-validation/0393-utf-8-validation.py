class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        bytes_to_process = 0
        
        for num in data:
            if bytes_to_process == 0:
                # Determine how many bytes the UTF-8 character has
                if (num >> 7) == 0b0:
                    bytes_to_process = 0
                elif (num >> 5) == 0b110:
                    bytes_to_process = 1
                elif (num >> 4) == 0b1110:
                    bytes_to_process = 2
                elif (num >> 3) == 0b11110:
                    bytes_to_process = 3
                else:
                    return False
            else:
                # For continuation bytes, check that they start with '10'
                if (num >> 6) != 0b10:
                    return False
                bytes_to_process -= 1
                
        # Return True only if we successfully processed all expected continuation bytes
        return bytes_to_process == 0