public class Solution {
    
    // Time complexity : O(N), because the entire tree is traversed only once in the worst case, 
    // and there are N nodes in the tree

    // Space complexity : O(N), because the size of the set can grow up to N in the worst case, where N are the nodes of the tree

    
    public boolean findTarget(TreeNode root, int k) {
        
        Set <Integer> set = new HashSet();
        
        return find(root, k, set);
        
    }
    
    
    public boolean find(TreeNode root, int k, Set < Integer > set) {
       if (root != null) {
            int complement = k - root.val;
            if (set.contains(complement)) {
                return true;
            }
            else {
                set.add(root.val);
            }
           return find(root.left,k,set) || find(root.right,k,set);
       }
        // base case
       else {
           return false;
       }
    }
}
