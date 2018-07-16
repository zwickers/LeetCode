class Solution {
    
    public int hammingDistance(int x, int y) {
        
        int xor = x ^ y;
        int counter = 0;
        
        // integers are 32 bits
        for (int i = 0; i < 32; i++) {
            counter += (xor >> i) & 1;
        }
        
        return counter;
        
    }
}
