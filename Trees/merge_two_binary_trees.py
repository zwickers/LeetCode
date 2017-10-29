# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        # base case: None node on both trees
        if not t1 and not t2:
            return None

        value = None
        node = None

        if t1 and not t2:
            node = TreeNode(t1.val)
        if t2 and not t1:
            node = TreeNode(t2.val)
        if t1 and t2:
            node = TreeNode(t1.val + t2.val)

        node.left = self.mergeTrees(t1.left if t1 else None,t2.left if t2 else None)
        node.right = self.mergeTrees(t1.right if t1 else None, t2.right if t2 else None)

        return node
