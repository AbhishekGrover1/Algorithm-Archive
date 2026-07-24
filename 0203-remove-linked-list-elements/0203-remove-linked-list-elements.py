class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        # Create a dummy node pointing to the head to handle edge cases easily
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        
        # Traverse the linked list
        while curr.next:
            if curr.next.val == val:
                # Bypass the node with the target value
                curr.next = curr.next.next
            else:
                # Advance pointer if no removal
                curr = curr.next
                
        return dummy.next