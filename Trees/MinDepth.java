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
    
    // time complexity: O(N), where N is the number of nodes in the tree
    // space complexity: O(N), BFS will have to store at least an entire level of the tree in the queue,
    // and in a perfect fully-balanced binary search tree, that would be (N/2 + 1) nodes in the last level
    
    public int minDepth(TreeNode root) {
        
        // base case: node is null
        if (root == null) {
            return 0;
        }
        
        Queue<TreeNode> q = new LinkedList<TreeNode>();
        q.offer(root);
        int size = q.size();
        int levels = 1;
        
        // BFS
        while (!q.isEmpty()) {
            for (int i = 0; i < size; i++) {
                TreeNode node = q.poll();
                if (node.left == null && node.right == null) {
                    return levels;
                }
                if (node.left != null) {
                    q.offer(node.left);
                }
                if (node.right != null) {
                    q.offer(node.right);
                }
            }
            levels++;
            size = q.size();
        }
        
        // something is very very wrong if this line ever runs lmao...
        return -1;
        
    }
}
