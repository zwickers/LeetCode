# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    # iterative solution using
    # Breadth-First Search (BFS)
    # O(n) time complexity
    
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        queue = [root]
        
        while queue:
            level = [i.val if i else None for i in queue]
            
            # the tree is symmetric if each level of the tree is the same forward-and-backward
            if level != level[::-1]:
                return False
            else:
                queue = [child for i in queue if i for child in (i.left,i.right)]

        return True
