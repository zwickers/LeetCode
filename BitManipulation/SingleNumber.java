class Solution {
    
    // xor is associative, so it doesn't matter what order you perform it in.
    // when you xor a number with itself, the result is 0 
    // so if you xor every integer in the array with eachother, the result will be the unique number
    
    // TIME COMPLEXITY: O(n), where n is the number of elements in the array
    // SPACE COMPLEXITY: O(1)
    
    public int singleNumber(int[] nums) {
        
        int result = 0;
        
        for (Integer num : nums) {
            result = result ^ num;
        }
        
        return result;
        
    }
}
