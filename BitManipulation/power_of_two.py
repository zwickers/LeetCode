class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """       
        
        if n <= 0:
            return False
        
        # n & n-1 returns the value of n with the lowest set bit erased
        if (n & (n-1)) == 0:
            return True
        else:
            return False
        
