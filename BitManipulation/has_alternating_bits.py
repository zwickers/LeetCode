class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # convert n to a string of bits
        # and remove the '0b' at the beginning
        str_bin = bin(n)[2:]
        
        # if two bits in a row are ever the same number,
        # then return false
        for i,c in enumerate(str_bin):
            if i==0:
                continue
            if str_bin[i] == str_bin[i-1]:
                return False
        
        return True
