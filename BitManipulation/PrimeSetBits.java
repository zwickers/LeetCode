class Solution {
    public int countPrimeSetBits(int L, int R) {
        
        int numOfPrimeSetBits = 0;
        
        for (int num = L; num <= R; num++) {
            
            int setBits = 0;
            
            for (int i = 0; i < 32; i++) {
                if (((num >>> i) & 1) == 1)  setBits++;
            }
            
            if (isPrime(setBits)) {
                numOfPrimeSetBits++;
            }
            
        }
        
        return numOfPrimeSetBits;
        
    }
    
    private boolean isPrime(int num) {
        
        // 1 is not a prime number
        if (num <= 1) return false;
            
        for (int i = 2; i*i <= num; i++) {
            if (num%i==0) return false; 
        }
        
        return true;
    }
    
}
