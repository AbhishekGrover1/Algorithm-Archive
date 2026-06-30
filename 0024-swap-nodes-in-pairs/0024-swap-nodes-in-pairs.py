# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Create a dummy node that points to the head
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        
        # Loop while there are at least two nodes left to swap
        while current.next is not None and current.next.next is not None:
            first = current.next
            second = current.next.next
            
            # Form the swapped links
            current.next = second
            first.next = second.next
            second.next = first
            
            # Move current forward by two nodes for the next pair
            current = first
            
        return dummy.next
        