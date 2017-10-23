class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # PATTERN:
        # 4^0 = 1  = 1
        # 4^1 = 4  = 100
        # 4^2 = 16 = 10000
        # 4^3 = 64 = 1000000
        # i.e., MSB is 1, all other bits are 0, and there are an odd number of bits
        
        if num == 1:
            return True
        if bin(num)[2] == '1' and bin(num)[3:].count('1') == 0 and len(bin(num)[2:]) % 2 != 0:
            return True
        else:
            return False
