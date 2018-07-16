class Solution {
    
    //TIME COMPLEXITY: O(1)
    //SPACE COMPLEXITY: O(1)
    
    public boolean hasAlternatingBits(int n) {
        
        //get rightmost bit
        int curr = n & 1;
        //do a right bitshift
        n >>= 1;
        
        while (n > 0) {
            
            if ((n & 1) == curr) {
                return false;
            }
            
            //get rightmost bit
            curr = n & 1;
            //do a right bitshift
            n >>= 1;
        }
        
        return true;
        
    }
}
