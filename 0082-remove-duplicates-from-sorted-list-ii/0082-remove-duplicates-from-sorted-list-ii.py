# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         #     self.val = val
#         #     self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Sentinel node to handle edge cases where the head itself needs to be deleted
        dummy = ListNode(0)
        dummy.next = head
        
        # 'prev' is the last known node before a sequence of duplicates
        prev = dummy
        
        while head:
            # If we detect the start of a duplicate sequence
            if head.next and head.val == head.next.val:
                # Move 'head' forward until we reach the last node of this duplicate sequence
                while head.next and head.val == head.next.val:
                    head = head.next
                # Skip all duplicates by linking 'prev' directly to the node after the sequence
                prev.next = head.next
            else:
                # No duplicates found for this value; safe to advance 'prev'
                prev = prev.next
                
            # Move 'head' forward to continue the scan
            head = head.next
            
        return dummy.next