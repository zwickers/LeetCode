class Solution {
    public int singleNumber(int[] nums) {
        
        int res = 0;
        int sum=0;
        
        
        // sum corresponding bits from all elements and mod each by 3 then should left the single number
        for (int i = 0; i < 32; i++) {
            
            for (int j = 0; j < nums.length; j++) {
                
                // sum every bit of all numbers
                sum += ((nums[j] >> i) & 1);
                
            }
            
            sum %= 3;
            res += sum << i;
            sum = 0;
        
        }
        
        return res;
    }
}
