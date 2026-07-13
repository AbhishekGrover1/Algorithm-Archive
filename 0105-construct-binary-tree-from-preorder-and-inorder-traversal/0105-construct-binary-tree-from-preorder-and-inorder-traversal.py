# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        # Map to quickly find the index of a value in the inorder list
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        # Pointer to track the current root element in preorder
        self.pre_idx = 0
        
        def helper(left_in, right_in):
            # If there are no elements to construct the subtree
            if left_in > right_in:
                return None
            
            # Select the current preorder element as the root
            root_val = preorder[self.pre_idx]
            root = TreeNode(root_val)
            self.pre_idx += 1
            
            # Find the index of this root in the inorder list
            in_idx = inorder_map[root_val]
            
            # Build left and right subtrees
            # Crucial: Left subtree must be built first because preorder sequences root -> left -> right
            root.left = helper(left_in, in_idx - 1)
            root.right = helper(in_idx + 1, right_in)
            
            return root
            
        return helper(0, len(inorder) - 1)