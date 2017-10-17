# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
        ###########################################################################
        # BASE CASES:
        ###########################################################################
        # if a node exists on one tree but not the other, the trees are not the same
        if p and not q:
            return False
        if not p and q:
            return False
        # if you have recursed all the way through a branch without returning
        # false, that branch is identitical on both trees
        if not p and not q:
            return True
        
        ###########################################################################
        # RECURSIVE STEP:
        ###########################################################################
        # if a node exists on both trees
        # with the same value, continue recursing through the tree
        if p and q and p.val == q.val:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        else:
            return False
