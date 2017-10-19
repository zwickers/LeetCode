# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return None
        
        # first, get rid of the nodes at
        # the beginning of the LL that 
        # have the unwanted val
        while head and head.val == val:
            head = head.next
    
        curr = head
        
        while curr and curr.next:
            # have the current node's
            # "next" pointer skip the next node
            # if the next node contains the unwanted
            # value
            if curr.next.val == val:
                curr.next = curr.next.next
            # if the next node does not have the
            # unwanted value, simply keep traversing
            # the list
            else:
                curr = curr.next
        
        return head
