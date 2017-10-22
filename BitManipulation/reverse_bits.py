class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        
        # convert n to string of bits and remove
        # the '0b' at the beginning
        str_bin = bin(n)[2:]
        
        # pad with 0s
        str_bin = (32-len(str_bin))*'0' + str_bin
        
        # add the '0b' to the beginning of the reversed string
        str_bin = '0b' + str_bin[::-1]
        
        # convert back into an integer and return the value
        return int(str_bin, 2)
