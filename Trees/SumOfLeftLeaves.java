/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public int sumOfLeftLeaves(TreeNode root) {
        
        // base case: the node is null
        if (root == null) {
            return 0;
        }
        
        // recursive case #1: left child is a leaf
        // return the value of the left leaf + sumOfLeftLeaves() of the right subtree
        if (root.left != null && root.left.left == null && root.left.right == null) {
            return root.left.val + sumOfLeftLeaves(root.right);
        }
        
        // recursive case #2: left child is not a leaf
        // return the sumOfLeftLeaves() of the left subtree + sumOfLeftLeaves() of the right subtree
        return sumOfLeftLeaves(root.left) + sumOfLeftLeaves(root.right);
        
    }
    
}
