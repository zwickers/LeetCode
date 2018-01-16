class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
       
        # 0x5 is 0101
        return (num > 0) and (num & (num - 1) == 0) and (num & 0x55555555 == num)
    
