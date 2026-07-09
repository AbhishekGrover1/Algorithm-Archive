# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        res = []
        stack = []
        curr = root
        
        while curr or stack:
            # Reach the left most Node of the curr Node
            while curr:
                stack.append(curr)
                curr = curr.left
                
            # Current must be None at this point
            curr = stack.pop()
            res.append(curr.val) # Add the parent node value
            
            # We have visited the node and its left subtree. 
            # Now, it's the right subtree's turn.
            curr = curr.right
            
        return res