# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        result = []
        
        def dfs(node, remaining_sum, current_path):
            if not node:
                return
            
            # Add the current node's value to the path
            current_path.append(node.val)
            
            # Check if it is a leaf node and the path sum matches targetSum
            if not node.left and not node.right and remaining_sum == node.val:
                result.append(list(current_path))
            else:
                # Continue searching the left and right subtrees
                dfs(node.left, remaining_sum - node.val, current_path)
                dfs(node.right, remaining_sum - node.val, current_path)
            
            # Backtrack: remove the current node before returning up the recursion tree
            current_path.pop()
            
        dfs(root, targetSum, [])
        return result