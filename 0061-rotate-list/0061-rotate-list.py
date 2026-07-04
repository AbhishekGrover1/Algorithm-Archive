# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # Edge case: empty list, single node, or no rotation needed
        if not head or not head.next or k == 0:
            return head
        
        # 1. Compute the length of the list and find the tail
        last_node = head
        length = 1
        while last_node.next:
            last_node = last_node.next
            length += 1
            
        # 2. Make the linked list circular
        last_node.next = head
        
        # 3. Find the new tail position
        # If length is 5 and k is 2, the new tail is at index (5 - 2) = 3rd node from head
        effective_k = k % length
        steps_to_new_tail = length - effective_k
        
        new_tail = head
        for _ in range(steps_to_new_tail - 1):
            new_tail = new_tail.next
            
        # 4. Set the new head and break the ring
        new_head = new_tail.next
        new_tail.next = None
        
        return new_head