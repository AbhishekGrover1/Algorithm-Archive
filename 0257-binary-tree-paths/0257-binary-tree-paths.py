# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        paths = []
        if not root:
            return paths

        def dfs(node, current_path):
            # If it's a leaf node, add the complete path to the results
            if not node.left and not node.right:
                paths.append(current_path)
                return

            if node.left:
                dfs(node.left, current_path + "->" + str(node.left.val))
            if node.right:
                dfs(node.right, current_path + "->" + str(node.right.val))

        dfs(root, str(root.val))
        return paths