class Solution {
    public int[] countBits(int num) {
        
        int[] nums = new int[num+1];
        
        for (int i = 0; i <= num; i++) {
            
            int count = 0;
            
            for (int offset = 0; offset < 32; offset++) {
                if (((i >> offset) & 1) == 1) count++;
            }
            
            nums[i] = count;
            
        }
        
        return nums;
        
    }
}
