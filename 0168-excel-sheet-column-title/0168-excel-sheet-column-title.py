class Solution(object):

  def convertToTitle(self, columnNumber):
    """:type columnNumber: int

    :rtype: str
    """
    result = []

    while columnNumber > 0:
      # Subtract 1 to shift from 1-based indexing (A=1...Z=26)
      # to 0-based indexing (A=0...Z=25)
      columnNumber -= 1
      remainder = columnNumber % 26
      result.append(chr(ord('A') + remainder))
      columnNumber //= 26

    return ''.join(reversed(result))