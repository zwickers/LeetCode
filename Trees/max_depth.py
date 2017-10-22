# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # base case: if current node is None, return 0
        if not root:
            return 0
        
        # recursive case: if current node does exist, add 1 to the
        # max() of the left and right subtrees
        return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))
