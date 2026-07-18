"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root
        
        # Start with the root node. The left child will be the start of the next level.
        leftmost = root
        
        while leftmost.left:
            # Iterate through the current level using the next pointers
            curr = leftmost
            while curr:
                # Connection 1: Children of the same parent
                curr.left.next = curr.right
                
                # Connection 2: Children between adjacent subtrees
                if curr.next:
                    curr.right.next = curr.next.left
                
                # Move to the next node on the current level
                curr = curr.next
                
            # Move down to the next level
            leftmost = leftmost.left
            
        return root