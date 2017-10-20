# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr = head
        while curr and curr.next:
            # Because the input list is sorted,
            # you can determine if a node is a duplicate 
            # by comparing its value to the node after it in the list. 
            if curr.val == curr.next.val:
                # if it is, "skip" the next node
                # by changing the next pointer
                curr.next = curr.next.next
            else:
                # otherwise, keep traversing the linked list
                curr = curr.next
        return head
