# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        # Dummy nodes to easily track the heads of the two queues
        less_head = ListNode(0)
        greater_head = ListNode(0)
        
        # Pointers to move along and build the two lists
        less = less_head
        greater = greater_head
        
        current = head
        while current:
            if current.val < x:
                less.next = current
                less = less.next
            else:
                greater.next = current
                greater = greater.next
            current = current.next
        
        # Prevent cycles by terminating the greater list
        greater.next = None
        
        # Connect the end of the 'less' list to the start of the 'greater' list
        less.next = greater_head.next
        
        return less_head.next