class Solution {
    public boolean isPowerOfFour(int num) {
        
        int bitMask = 0xAAAAAAAA; //...10101010
        
        // (num & (num-1)) == 0 checks to make sure the number is a power of 2 (every power of 4 is also a power of 2)
        // (num & bitMask) == 0 checks to make sure that there are an even number of 0s after the 1
        
        return ((num & (num-1)) == 0) && ((num & bitMask) == 0) && num > 0;
        
    }
}
