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
    
    // TIME COMPLEXITY: O(N), where N is the number of nodes
    public int maxDepth(TreeNode root) {
        
        if (root == null) {
            return 0;
        }
        
        int leftSubtree = 1 + maxDepth(root.left);
        int rightSubtree = 1 + maxDepth(root.right);
        
        return Math.max(leftSubtree, rightSubtree);
        
    }
}
