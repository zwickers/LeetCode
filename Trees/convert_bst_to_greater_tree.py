# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    
    
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        # keep track of the the value of the node last visited
        self.val = 0
        
        def transform(curr):
            
            # base case: if the node is None, return
            if not curr:
                return

            # do a reverse in-order traversal of the BST (right subtree --> current node --> left subtree)
            # this will give the keys in decreasing order
            
            transform(curr.right)

            # add the value of the last visited node (self.val)
            # to the current node
            curr.val += self.val
            self.val = curr.val

            transform(curr.left)
        
        transform(root)
        
        return root
