# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        # Map values to their indices in inorder traversal for O(1) lookups
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        def helper(left_idx, right_idx):
            # Base case: if there are no elements to construct the subtree
            if left_idx > right_idx:
                return None
            
            # The last element of postorder is the current root node
            root_val = postorder.pop()
            root = TreeNode(root_val)
            
            # Root splits inorder list into left and right subtrees
            pivot = inorder_map[root_val]
            
            # CRITICAL: Build right subtree first because postorder elements 
            # are consumed from right to left (root -> right -> left)
            root.right = helper(pivot + 1, right_idx)
            root.left = helper(left_idx, pivot - 1)
            
            return root
            
        return helper(0, len(inorder) - 1)