# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):

  def recoverTree(self, root):
    """:type root: Optional[TreeNode]

    :rtype: None Do not return anything, modify root in-place instead.
    """
    first = second = prev = None
    curr = root

    # Morris Inorder Traversal for O(1) auxiliary space
    while curr:
      if not curr.left:
        # Process current node
        if prev and prev.val > curr.val:
          if not first:
            first = prev
          second = curr
        prev = curr
        curr = curr.right
      else:
        # Find the inorder predecessor of curr
        pred = curr.left
        while pred.right and pred.right != curr:
          pred = pred.right

        if not pred.right:
          # Make curr the right child of its predecessor
          pred.right = curr
          curr = curr.left
        else:
          # Revert the changes made in the tree structure
          pred.right = None
          if prev and prev.val > curr.val:
            if not first:
              first = prev
            second = curr
          prev = curr
          curr = curr.right

    # Swap the values of the two mismatched nodes
    if first and second:
      first.val, second.val = second.val, first.val