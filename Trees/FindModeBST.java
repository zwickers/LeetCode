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
    
    // Strategy: fill up a hashmap where the key's are the integers from the tree,
    // and the value's are the frequency
    
    // then loop through the hashmap to find the mode
    
    // then loop through the hashmap and fill up a HashSet with the elements that appear *mode* number of times
    
    // then put them in an array and return it
    
    
    // TIME COMPLEXITY: O(N), where N are the nodes in the tree
    // SPACE COMPLEXITY: O(N)
    public int[] findMode(TreeNode root) {
        
        HashMap<Integer,Integer> map = new HashMap<>();
        
        fillMap(root,map);
        
        int mode = 1;     
        
        for (int val : map.values()) {
            mode = Math.max(mode,val);
        }
        
        HashSet<Integer> set = new HashSet<>();
        
        for (int key : map.keySet()) {
            if (map.get(key) == mode) set.add(key);
        }
        
        int[] arr = new int[set.size()];
        int idx = 0;
        
        for (int num : set) {
            arr[idx++] = num;
        }
        
        return arr;
        
    }
    
    public void fillMap(TreeNode root,HashMap<Integer,Integer> map) {
        if (root != null) {
            fillMap(root.left,map);
            fillMap(root.right,map);
            if (!map.containsKey(root.val)) {
                map.put(root.val, 1);
            } 
            else {
                map.put(root.val, 1 + map.get(root.val));
            }
        }
    }
}
