# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Create a dummy node to hold the head of the merged list
        dummy = ListNode(0)
        tail = dummy
        
        # Iterate while both lists have elements
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            # Move the tail pointer forward
            tail = tail.next
            
        # Append the remaining nodes of list1 or list2
        if list1 is not None:
            tail.next = list1
        else:
            tail.next = list2
            
        # The merged list starts from dummy.next
        return dummy.next