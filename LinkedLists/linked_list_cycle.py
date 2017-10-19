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
        # This can be solved using 
        # Floyd's cycle-finding algorithm
        fast = head
        slow = head
        # have two pointers, moving at different rates,
        # traverse the list. they will point to the same node
        # at some point if there is a cycle
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False
            
        
        
        
