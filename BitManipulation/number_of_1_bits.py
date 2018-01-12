class Solution(object):
    
    # time complexity: O(k), where k is the number of 1-bits
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n:
            # n & (n-1) is equal to n with it's lowest 1 bit erased
            n = n & (n-1)
            count += 1
        return count
       
