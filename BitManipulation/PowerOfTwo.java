class Solution {
    
    public boolean isPowerOfTwo(int n) {
        // check that the number is just a 1 followed by 0s, and that it is positive
        return ((n & (n-1)) == 0) && n > 0;
    }
    
}
