class Solution {
    
    // you are only flipping the bits including and
    // to the right of the first 1 bit, so you need a bit-mask
    
    public int findComplement(int num) {
        
        int counter = 0;
        
        for (int i = 0; i < 31; i++) {
            if (((num >> i) & 1) == 1) 
                counter = i + 1;
        }
        
        int bitMask = (1 << counter) - 1;
        
        return (~num) & bitMask;
        
    }
}
