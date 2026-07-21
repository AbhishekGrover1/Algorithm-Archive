# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next          # moves 1 step at a time
            fast = fast.next.next     # moves 2 steps at a time
            
            # If fast and slow pointers meet, a cycle exists
            if slow == fast:
                return True
        
        # Fast reached the end of the list, no cycle
        return False