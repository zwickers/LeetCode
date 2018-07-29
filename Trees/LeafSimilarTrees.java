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
    
    // The approach is simple: do an in-order DFS of both trees
    // and store all the leaves that you encounter in two separate lists
    // then, compare the lists.
    
    // TIME COMPLEXITY: O(T1 + T2), where T1 and T2 are the lengths of the given trees.
    // SPACE COMPLEXITY: O(T1 + T2), the space used in storing the leaf values. 
    
    public boolean leafSimilar(TreeNode root1, TreeNode root2) {
        
        ArrayList<Integer> leaf1 = new ArrayList<>();
        ArrayList<Integer> leaf2 = new ArrayList<>();

        dfs(leaf1,root1);
        dfs(leaf2, root2);
    
        return leaf1.equals(leaf2);
        
    }
    
    public void dfs(ArrayList<Integer> leafs, TreeNode root) {

        if (root != null) {

            dfs(leafs, root.left);
            
            
            if (root.left == null && root.right == null) {
                leafs.add(root.val);
            }
            
            dfs(leafs, root.right);
            
        }    
        
    }
}
