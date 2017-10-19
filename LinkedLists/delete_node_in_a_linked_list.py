# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # change the value of the current node to the next node's value
        # then make this node point 2 nodes ahead, causing the node after
        # it to get destroyed via garbage collection.
        # this effectively "removes" the node that was passed in as a parameter
        node.val = node.next.val
        node.next = node.next.next
