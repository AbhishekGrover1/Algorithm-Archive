# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[TreeNode]
        """
        # Step 1: Convert the linked list to an array
        values = []
        current = head
        while current:
            values.append(current.val)
            current = current.next
            
        # Step 2: Use the array to build a balanced BST
        def build_bst(left, right):
            if left > right:
                return None
            
            # Find the middle index
            mid = (left + right) // 2
            
            # Create the root node
            root = TreeNode(values[mid])
            
            # Recursively build left and right branches
            root.left = build_bst(left, mid - 1)
            root.right = build_bst(mid + 1, right)
            
            return root
            
        # Initialize the recursion with the full array bounds
        return build_bst(0, len(values) - 1)