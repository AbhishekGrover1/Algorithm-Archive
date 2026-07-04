# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # If the list is empty or has only one node, no duplicates can exist
        if not head:
            return head
        
        current = head
        
        # Traverse the list until the end
        while current and current.next:
            if current.val == current.next.val:
                # Duplicate found, skip the next node
                current.next = current.next.next
            else:
                # No duplicate, move to the next node
                current = current.next
                
        return head