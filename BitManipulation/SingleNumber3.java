class Solution {
    
    // time complexity: O(N)
    // space complexity: O(1)
    public int[] singleNumber(int[] nums) {
        
        // let A and B be the two unique elements
        // first, XOR everything together, this will be equal to A XOR B since everything else will cancel out
        
        int xor = 0;
        
        for (int i = 0; i < nums.length; i++) {
            xor ^= nums[i];
        }
        
        // The 2 unique numbers...their bits will differ in atleast one position, which would be the 1's in XOR. 
        // We will take the rightmost such 1 from the XOR, but technically you can pick any bit
        // This 1 must have come from either numbers, to identify which, we XOR all numbers into 2 sets, one set which had that bit set and one which didn't. In the end, the duplicate numbers will cancel themselves out leaving only the unique numbers in each set.
        
        int bit = xor & ~(xor-1); 
        
        int[] res = new int[2];
        
        for (int num : nums) {
            if ((num & bit) > 0) {
                res[0] ^= num;
            }
            else {
                res[1] ^= num;
            }
        }
        
        return res;
        
        
    }
}
