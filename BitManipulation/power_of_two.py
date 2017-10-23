class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """       
        # edge case: n == 1, in this case there are no zero's at all because
        # of the way python stores binary numbers
        # '0b1'
        if n == 1:
            return True
        
        # if the MSB is a 1 and all other bits
        # are 0s, then it is a power of 2
        if bin(n)[2] == '1' and bin(n)[3:].count('1') == 0:
            return True
        else:
            return False
