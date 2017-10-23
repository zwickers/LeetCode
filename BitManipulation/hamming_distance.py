class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # a bitwise XOR will yield a binary number
        # where there is a 1 in each binary digit where x and y differ
        
        # convert the result to a string using bin(), and count the number of 1's
        return bin(x ^ y).count('1')
