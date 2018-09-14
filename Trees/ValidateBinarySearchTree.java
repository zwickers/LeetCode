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
    
    // TIME COMPLEXITY: O(n), where n is the number of nodes
    // SPACE COMPLEXITY: O(1)
    
    public boolean isValidBST(TreeNode root) {
        
        return isValidBSTUtil(root, Long.MAX_VALUE, Long.MIN_VALUE);
        
    }
    
    //traverse the tree, looking at each node only once, while progressively narrowing the allowed min and max values
    private boolean isValidBSTUtil(TreeNode node, long max, long min) {
        
        // an empty tree is a valid BST :^)
        if (node == null) return true;
        
        if (node.val <= min || node.val >= max) return false;
        
        return isValidBSTUtil(node.left,node.val,min) && isValidBSTUtil(node.right,max,node.val);
        
    }
    
}
