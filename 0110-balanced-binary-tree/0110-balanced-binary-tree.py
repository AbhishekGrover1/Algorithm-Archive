# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def check_height(node):
            # Base case: an empty tree is balanced and has a height of 0
            if not node:
                return 0
            
            # Check the left subtree
            left_height = check_height(node.left)
            # If the left subtree is unbalanced, propagate the -1 up
            if left_height == -1:
                return -1
                
            # Check the right subtree
            right_height = check_height(node.right)
            # If the right subtree is unbalanced, propagate the -1 up
            if right_height == -1:
                return -1
                
            # If the current node is unbalanced, return -1
            if abs(left_height - right_height) > 1:
                return -1
                
            # Otherwise, return the height of the tree rooted at this node
            return max(left_height, right_height) + 1
            
        # The tree is balanced if the helper function doesn't return -1
        return check_height(root) != -1