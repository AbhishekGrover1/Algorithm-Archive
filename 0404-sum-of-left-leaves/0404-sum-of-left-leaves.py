class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        
        total_sum = 0
        
        # Check if the left child exists and is a leaf node
        if root.left and not root.left.left and not root.left.right:
            total_sum += root.left.val
        else:
            # Otherwise, continue searching down the left subtree
            total_sum += self.sumOfLeftLeaves(root.left)
            
        # Continue searching down the right subtree
        total_sum += self.sumOfLeftLeaves(root.right)
        
        return total_sum