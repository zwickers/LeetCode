# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #base case, current node is None
        if not root:
            return 0
        
        #recursive case 1: left child is a leaf
        #in this case, just return the value of the left child
        #plus the sumOfLeftLeaves() of right child
        if root.left and not root.left.left and not root.left.right:
            return root.left.val + self.sumOfLeftLeaves(root.right)
        
        #recursive case 2: left child is NOT a leaf
        #sum the left leaves of the left subtree and the right subtree
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
