class Solution:
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        
        result = 0
        
        # idea: add 2^{32-1-i} to result for each 1-bit,      
        for i in range(32):
            if (n >> i) & 1:
                result += 2 ** (32-1-i)
                
        return result
