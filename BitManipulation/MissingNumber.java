class Solution {
    
    //time complexity: O(N)
    //space complexity: O(1)
    
    public int missingNumber(int[] nums) {
        
        int xor = nums.length;
        
        for (int i = 0; i < nums.length; i++) {
            xor ^= i ^ nums[i];
        }
        
        return xor;
        
    }
}
