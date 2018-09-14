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
    // time complexity: O(n)
    // space complexity: O(1)
    public TreeNode searchBST(TreeNode root, int val) {
        if(root == null) return root;
        if(root.val == val){
            return root;
        }
        else{
            return root.val > val ? searchBST(root.left,val) : searchBST(root.right,val);
        }
    }
}
